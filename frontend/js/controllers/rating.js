main.controller('rating', function ($scope, $http, $location, $cookies) {
    //контроллер страницы rating
    $scope.$parent.pageName = 'rating';
    //получаем ссылочку
    let urls = new BackendConnector();

    $.ajax({
        url: urls.domain + 'user/list/',
        method: 'get',
        datatype: 'application/json',
        success: function (data) {
            let api = new Api();
            $scope.userList = data
            //подсчитываем у каждого их пассивный доход
            for (i=0; i<$scope.userList.length; i++) {
                //считаем пассивный доход
                $scope.userList[i].passiveIncome = 0;
                for (j=0; j<$scope.userList[i].providers.length; j++) {
                    $scope.userList[i].passiveIncome = $scope.userList[i].passiveIncome + $scope.userList[i].providers[j].count * $scope.userList[i].providers[j].provider.income;
                }
                //считаем работу администрации
                $scope.userList[i].adminsProfit = 0;
                for (j=0; j<$scope.userList[i].admins.length; j++) {
                    $scope.userList[i].adminsProfit = $scope.userList[i].adminsProfit + $scope.userList[i].admins[j].count * $scope.userList[i].admins[j].admin.profit;
                }
                if ($scope.userList[i].adminsProfit > 100) { //максимум - 100%
                    $scope.userList[i].adminsProfit = 100;
                }
                $scope.userList[i].passive_income = $scope.userList[i].passiveIncome * $scope.userList[i].adminsProfit / 100;
            }
            //сортируем по сахару за все время по убыванию
            $scope.userList.sort(api.byFieldUp('sugar_all_time'));

            //расставляем номера
            for (i=0; i < $scope.userList.length; i++) {
                $scope.userList[i].number = i+1
            }

            $scope.$apply();

            console.log($scope.userList);
        }
    });
    //при клике кнопки параметры
    $scope.changeSorting = function (where) {
        let api = new Api();
        let selected = document.querySelector('input[name="radio2"]:checked');
        if (selected.id == "btnradio-small1" || selected.id == "btnradio-small3") {
            $scope.userList.sort(api.byFieldUp(where));
        } else {
            $scope.userList.sort(api.byFieldDown(where));
        }

        //расставляем номера
        for (i=0; i < $scope.userList.length; i++) {
            $scope.userList[i].number = i+1
        }

        $scope.$apply();
    }

    //при клике по кнопке возрастание-убывание
    $scope.changeSortingUpToDown = function (where) {
        let api = new Api();
        let selectedClassList = document.querySelector('input[name="radio"]:checked').classList;
        // вторым элементом лежит изменяемое значение
        if (where == 'down') {
            $scope.userList.sort(api.byFieldUp(selectedClassList[1]));
        } else {
            $scope.userList.sort(api.byFieldDown(selectedClassList[1]));
        }

        //расставляем номера
        for (i=0; i < $scope.userList.length; i++) {
            $scope.userList[i].number = i+1
        }

        $scope.$apply();
    }
});