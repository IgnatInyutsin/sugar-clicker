from rest_framework import viewsets
from rest_framework.response import Response
from djangoProject.app.serializers.admins_group import AdminsGroupSerializer
from djangoProject.models import User, AdminsGroup
from djangoProject.models import Admin
from rest_framework.serializers import ValidationError
import time
from django.core import serializers

# Класс для запросов по регистрации, доступен только POST
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
            # по id соединяем с User
            user_for_update = User.objects.all().filter(id=request.POST['user.id'])
            #костыль, исправлю
            try:
                user = User.objects.all().filter(id=request.POST['user.id'])[0]
            except IndexError:
                raise ValidationError([{"code": "UNDEFINED_USER_ID", "text": "User ID is undefined"}])

            # по id соединяем с Admin
            try:
                admin = Admin.objects.all().filter(id=request.POST['admin.id'])[0]
            except IndexError:
                raise ValidationError([{"code": "UNDEFINED_ADMIN_ID", "text": "Admin ID is undefined"}])

            # проверяем, достаточная ли сумма на балансе
            if int(user.balance) >= int(admin.cost) * int(request.data['count']):
                # если да - снимаем нужную сумму с баланса
                user_for_update.update(balance=(int(user.balance) - int(admin.cost) * int(request.data['count'])))
            else:
                # иначе - ошибка
                raise ValidationError([{'code': 'SMALL_BALANCE', 'text': 'You do not have money'}])
            # Проверка на наличие группы. Если уже есть - обновляем, иначе - создаем.
            if not AdminsGroup.objects.all().filter(user_id=user).filter(admin_id=admin).exists():
                adminGroup = AdminsGroup(user_id=user, admin_id=admin, count=request.data['count'])
                adminGroup.save()
            else:  # иначе обновляем
                myAdminsGroup = AdminsGroup.objects.all().filter(user_id=user).filter(admin_id=admin)
                myAdminsGroup.update(count=(int(myAdminsGroup[0].count) + int(request.data['count'])))
            # Здесь будет автоматический сбор пассивного дохода

            return Response(status=201, data={"code": "SUCCESS_UPDATE_ADMINS", "text": "Your admins are updated"})

        # Иначе возвращаем сообщение о всех ошибках
        raise ValidationError(serializer.errors)

    def retrieve(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def update(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def partial_update(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})

    def destroy(self, request, pk=None):
        return Response(status=404,
                        data={"code": "INVALID_METHOD", "error_text": "Method is invalid for this path"})