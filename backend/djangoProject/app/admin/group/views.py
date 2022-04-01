from rest_framework import viewsets, mixins
from rest_framework.response import Response
from djangoProject.app.admin.group.serializers import AdminsGroupSerializer, AdminsGroupGetSerializer
from djangoProject.app.user.models import User
from djangoProject.app.admin.models import Admin, AdminsGroup
from rest_framework.serializers import ValidationError
import time
from django.core import serializers
import uuid
from djangoProject.app.user.passive_income.views import PassiveIncomeViewSet

# Класс для запросов по AdminsGroup, доступен только POST и GET
class AdminsGroupViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    #связываем с сериализатором
    queryset = AdminsGroup.objects.all().order_by('id')
    serializer_class = AdminsGroupGetSerializer

    # для разных методов разные сериализаторы
    def get_serializer_class(self):
        if self.action == 'create':
            return AdminsGroupSerializer
        else:
            return AdminsGroupGetSerializer

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
            if not Admin.objects.all().filter(id=request.POST['admin.id']).exists():
                raise ValidationError([{"code": "ADMIN_ID_UNDEFINED", "text": "admin_id in undefinded"}])

            # по session_id соединяем с User
            user_for_update = User.objects.all().filter(session_uuid=request.POST['user.session_uuid'])
            user = User.objects.all().filter(session_uuid=request.POST['user.session_uuid'])[0]
            # по id соединяем с Admin
            admin = Admin.objects.all().filter(id=request.POST['admin.id'])[0]

            # проверяем, достаточная ли сумма на балансе
            if int(user.balance) >= int(admin.cost) * int(request.data['count']):
                # если да - снимаем нужную сумму с баланса
                user_for_update.update(balance=(int(user.balance) - (int(admin.cost) * int(request.data['count']) )))
            else:
                # иначе - ошибка
                raise ValidationError([{'code': 'SMALL_BALANCE', 'text': 'You do not have money'}])

                # Собираем пассивный доход
                get_passive_income = PassiveIncomeViewSet()
                get_passive_income(user.id)

            # Проверка на наличие группы. Если уже есть - обновляем, иначе - создаем.
            if not AdminsGroup.objects.all().filter(user=user).filter(admin=admin).exists():
                adminGroup = AdminsGroup(user=user, admin=admin, count=int(request.data['count']))
                adminGroup.save()
            else:  # иначе обновляем
                myAdminsGroup = AdminsGroup.objects.all().filter(user=user).filter(admin=admin)
                myAdminsGroup.update(count=(int(myAdminsGroup[0].count) + int(request.data['count'])))

            # если все успешно возвращаем ответ
            return Response(status=201, data={"code": "SUCCESS_UPDATE_ADMINS", "text": "Your admins are updated"})

        # Если сериализатор не прошел валидацию, возвращаем ошибки
        raise ValidationError(serializer.errors)