from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.serializers.admins_group import AdminsGroupSerializer
from djangoProject.models import User, AdminsGroup
from djangoProject.models import Admin
from rest_framework.serializers import ValidationError
import time
from django.core import serializers

# Класс для запросов по AdminsGroup, доступен только POST и GET
class AdminsGroupViewSet(viewsets.ModelViewSet):
    #связываем с сериализатором
    queryset = AdminsGroup.objects.all().order_by('id')
    serializer_class = AdminsGroupSerializer

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
            if Admin.objects.all().filter(id=request.POST['admin.id']).exists():
                raise ValidationError([{"code": "ADMIN_ID_UNDEFINED", "text": "admin_id in undefinded"}])

            # по session_id соединяем с User
            user_for_update = User.objects.all().filter(session_uuid=request.POST['user.session_uuid'])
            user = User.objects.all().filter(session_uuid=request.POST['user.session_uuid'])[0]
            # по id соединяем с Admin
            admin = Admin.objects.all().filter(id=request.POST['admin.id'])[0]

            # проверяем, достаточная ли сумма на балансе
            if int(user.balance) >= int(admin.cost) * int(request.data['count']):
                # если да - снимаем нужную сумму с баланса
                user_for_update.update(balance=(int(user.balance) - int(admin.cost) * int(request.data['count'])))
            else:
                # иначе - ошибка
                raise ValidationError([{'code': 'SMALL_BALANCE', 'text': 'You do not have money'}])

            # Проверка на наличие группы. Если уже есть - обновляем, иначе - создаем.
            if not AdminsGroup.objects.all().filter(user_id=user).filter(admin_id=admin).exists():
                adminGroup = AdminsGroup(user_id=user.id, admin_id=admin.id, count=request.data['count'])
                adminGroup.save()
            else:  # иначе обновляем
                myAdminsGroup = AdminsGroup.objects.all().filter(user_id=user.id).filter(admin_id=admin.id)
                myAdminsGroup.update(count=(int(myAdminsGroup[0].count) + int(request.data['count'])))
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