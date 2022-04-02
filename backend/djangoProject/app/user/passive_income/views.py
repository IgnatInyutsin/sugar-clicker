from rest_framework import viewsets, mixins
from rest_framework.response import Response
from djangoProject.app.user.models import User
from djangoProject.app.provider.models import ProvidersGroup, Provider
from djangoProject.app.admin.models import Admin, AdminsGroup
from rest_framework.serializers import ValidationError
from rest_framework.decorators import api_view
from djangoProject.app.user.passive_income.serializers import PassiveIncomeSerializer
import time

class PassiveIncomeViewSet(mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = PassiveIncomeSerializer

    # PATCH
    def partial_update(self, request, pk):
        if pk.isdigit():
            serializer = self.get_serializer(data={
                "id": int(pk)
            })

            if serializer.is_valid(raise_exception=True):
                # получаем из бд данные об этом пользователе
                user = User.objects.get(id=pk)
                user_for_update = User.objects.all().filter(id=pk)
                # получаем всех админов и поставщиков
                providers = ProvidersGroup.objects.all().filter(user=user)
                admins = AdminsGroup.objects.all().filter(user=user)

                # считаем чистый пассивный доход
                clean_passive_income = 0
                for i in range(len(providers)):
                    clean_passive_income += providers[i].provider.income * providers[i].count

                # считаем работу администрации
                admin_profit = 0
                for i in range(len(admins)):
                    admin_profit += admins[i].admin.profit * admins[i].count

                # максимально - 100%
                if admin_profit > 100:
                    admin_profit = 100

                #считаем сколько получает пользователь в секунду
                passive_income = clean_passive_income * admin_profit / 100
                #считаем, сколько он получил
                income = passive_income * (time.time() - user.last_passive_income_data)

                #изменяем время последнего получения пассивного дохода и добавляем деньги
                user_for_update.update(last_passive_income_data=time.time(),
                            balance= user.balance + income,
                            sugar_all_time= user.sugar_all_time + income)

                #возвращаем сообщение об успешном изменении
                return Response(status=201, data={"code": "SUCCESS_PASSIVE_INCOME_UPDATE", "text": "passive_income is update!", "adding": income})

            raise ValidationError({"code": "USER_ID_UNDEFINDED", "text": "This user is undefined"})

        else:
            raise ValidationError({"code": "USER_ID_ISNT_NUMBER", "text": "User id is only number!"})

    # Для вызова извне
    def __call__(self, pk):
        # получаем из бд данные об этом пользователе
        user = User.objects.get(id=pk)
        user_for_update = User.objects.all().filter(id=pk)
        # получаем всех админов и поставщиков
        providers = ProvidersGroup.objects.all().filter(user=user)
        admins = AdminsGroup.objects.all().filter(user=user)

        # считаем чистый пассивный доход
        clean_passive_income = 0
        for i in range(len(providers)):
            clean_passive_income += providers[i].provider.income * providers[i].count

        # считаем работу администрации
        admin_profit = 0
        for i in range(len(admins)):
            admin_profit += admins[i].admin.profit * admins[i].count

        # максимально - 100%
        if admin_profit > 100:
            admin_profit = 100

        # считаем сколько получает пользователь в секунду
        passive_income = clean_passive_income * admin_profit / 100
        # считаем, сколько он получил
        income = passive_income * (time.time() - user.last_passive_income_data)

        # изменяем время последнего получения пассивного дохода и добавляем деньги
        user_for_update.update(last_passive_income_data=time.time(),
                               balance=user.balance + income,
                               sugar_all_time=user.sugar_all_time + income)