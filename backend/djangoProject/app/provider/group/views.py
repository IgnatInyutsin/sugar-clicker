from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from djangoProject.app.provider.group.serializers import ProvidersGroupSerializer, ProvidersGroupGetSerializer
from djangoProject.app.user.models import User
from djangoProject.app.provider.models import Provider, ProvidersGroup
from rest_framework.serializers import ValidationError
import time
from django.core import serializers
from rest_framework.renderers import JSONRenderer
import uuid
from djangoProject.app.user.passive_income.views import PassiveIncomeViewSet

# Класс для запросов по ProvidersGroup, доступен только POST и GET
class ProvidersGroupViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):

    #связываем с сериализатором
    queryset = ProvidersGroup.objects.all().order_by('id')
    serializer_class = ProvidersGroupGetSerializer

    # для разных методов разные сериализаторы
    def get_serializer_class(self):
        if self.action == 'create':
            return ProvidersGroupSerializer
        else:
            return ProvidersGroupGetSerializer

    # метод POST
    def create(self, request):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data=request.data)
        # Проверяем, все ли поля прошли валидацию
        if serializer.is_valid(raise_exception=True):
            # проверяем, актуальны ли admin_id и session_uuid (это должна сделать валидация в сериализаторе,
            # но она не работает, так что пусть сделает здесь)
            if not User.objects.all().filter(session_uuid=uuid.UUID(request.POST['user.session_uuid'])).exists():
                raise ValidationError([{"code": "SESSION_UUID_UNDEFINED", "text": "session_uuid in undefinded"}])
            if not Provider.objects.all().filter(id=request.POST['provider.id']).exists():
                raise ValidationError([{"code": "PROVIDER_ID_UNDEFINED", "text": "provider_id in undefinded"}])

            # по session_id соединяем с User
            user_for_update = User.objects.all().filter(session_uuid=request.POST['user.session_uuid'])
            user = User.objects.all().filter(session_uuid=request.POST['user.session_uuid'])[0]
            # по id соединяем с Admin
            provider = Provider.objects.all().filter(id=request.POST['provider.id'])[0]

            # проверяем, достаточная ли сумма на балансе
            if int(user.balance) >= int(provider.cost) * int(request.data['count']):
                # если да - снимаем нужную сумму с баланса
                user_for_update.update(balance=(int(user.balance) - (int(provider.cost) * int(request.data['count']) )))
            else:
                # иначе - ошибка
                raise ValidationError([{'code': 'SMALL_BALANCE', 'text': 'You do not have money'}])

            # Собираем пассивный доход
            get_passive_income = PassiveIncomeViewSet()
            get_passive_income(user.id)

            # Проверка на наличие группы. Если уже есть - обновляем
            if not ProvidersGroup.objects.all().filter(user=user).filter(provider=provider).exists():
                providersGroup = ProvidersGroup(user=user, provider=provider, count=request.data['count'])
                providersGroup.save()
            else:  # иначе обновляем
                myProvidersGroup = ProvidersGroup.objects.all().filter(user=user).filter(provider=provider)
                # проверяем max_count
                if provider.max_count != 0 \
                    and int(myProvidersGroup[0].count) + int(request.POST["count"]) > provider.max_count:
                    raise ValidationError([{"code": "MAX_COUNT",
                                            "text": "Count is very big for this provider",
                                            "max_count": provider.max_count}])

                myProvidersGroup.update(count=(int(myProvidersGroup[0].count) + int(request.data['count'])))

            # если все успешно возвращаем ответ
            return Response(status=201, data={"code": "SUCCESS_UPDATE_ADMINS", "text": "Your admins are updated"})

        # Если сериализатор не прошел валидацию, возвращаем ошибки
        raise ValidationError(serializer.errors)