from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.provider.group.serializer import ProvidersGroupSerializer
from djangoProject.app.user.models import User
from djangoProject.app.provider.models import Provider, ProvidersGroup
from rest_framework.serializers import ValidationError
import time
from django.core import serializers

# Класс для запросов по AdminsGroup, доступен только POST и GET
class ProvidersGroupViewSet(viewsets.ModelViewSet):
    #связываем с сериализатором
    queryset = ProvidersGroup.objects.all().order_by('id')
    serializer_class = ProvidersGroupSerializer

    # метод POST
    def create(self, request):
        # Получаем наш сериализатор
        serializer = self.get_serializer(data=request.data)
        # Проверяем, все ли поля прошли валидацию
        if serializer.is_valid(raise_exception=True):
            # проверяем, актуальны ли admin_id и session_uuid (это должна сделать валидация в сериализаторе,
            # но она не работает, так что пусть сделает здесь)
            if User.objects.all().filter(session_uuid=request.POST['user.session_uuid']).exists():
                raise ValidationError([{"code": "SESSION_UUID_UNDEFINED", "text": "session_uuid in undefinded"}])
            if Provider.objects.all().filter(id=request.POST['provider.id']).exists():
                raise ValidationError([{"code": "PROVIDER_ID_UNDEFINED", "text": "provider_id in undefinded"}])

            # по session_id соединяем с User
            user_for_update = User.objects.all().filter(session_uuid=request.POST['user.session_uuid'])
            user = User.objects.all().filter(session_uuid=request.POST['user.session_uuid'])[0]
            # по id соединяем с Admin
            provider = Provider.objects.all().filter(id=request.POST['provider.id'])[0]

            # проверяем, достаточная ли сумма на балансе
            if int(user.balance) >= int(provider.cost) * int(request.data['count']):
                # если да - снимаем нужную сумму с баланса
                user_for_update.update(balance=(int(user.balance) - int(provider.cost) * int(request.data['count'])))
            else:
                # иначе - ошибка
                raise ValidationError([{'code': 'SMALL_BALANCE', 'text': 'You do not have money'}])

            # Проверка на наличие группы. Если уже есть - обновляем, иначе - создаем.
            if not ProvidersGroup.objects.all().filter(user=user).filter(provider=provider).exists():
                providersGroup = ProvidersGroup(user=user, provider=provider, count=request.data['count'])
                providersGroup.save()
            else:  # иначе обновляем
                myProvidersGroup = ProvidersGroup.objects.all().filter(user=user).filter(provider=provider)
                myAdminsGroup.update(count=(int(myProvidersGroup[0].count) + int(request.data['count'])))
            # Здесь будет автоматический сбор пассивного дохода

            # если все успешно возвращаем ответ
            return Response(status=201, data={"code": "SUCCESS_UPDATE_ADMINS", "text": "Your admins are updated"})

        # Если сериализатор не прошел валидацию, возвращаем ошибки
        raise ValidationError(serializer.errors)

    def retrieve(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def update(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def partial_update(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})


    def destroy(self, request, pk=None):
        return Response(status=405,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})