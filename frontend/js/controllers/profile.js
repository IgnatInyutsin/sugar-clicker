main.controller('profile', function ($scope, $http, $location, $cookies, $routeParams) {
    //контроллер страницы profile
    $scope.$parent.pageName = 'profile';
    if ($scope.login) {
        let checker = new Api();
        checker.checkSession($cookies.get('session'), $cookies.get('user_id'))
    }
    let urls = new BackendConnector();

    // получаем данные о пользователе
    $.ajax({
        url: urls.domain + 'user/list/' + $routeParams.user + "/",
        method: 'get',
        datatype: 'application/json',
        success: function (data) {
            let api = new Api();
            $scope.aboutUser = data;
            // конвертируем время
            $scope.aboutUser.registration_at = api.timeConverter($scope.aboutUser.registration_at);
            //считаем пассивный доход
            $scope.passiveIncome = 0;
            for (i=0; i<$scope.aboutUser.providers.length; i++) {
                $scope.passiveIncome = $scope.passiveIncome + $scope.aboutUser.providers[i].count * $scope.aboutUser.providers[i].provider.income
            }
            //считаем работу администрации
            $scope.adminsProfit = 0
            for (i=0; i<$scope.aboutUser.admins.length; i++) {
                $scope.adminsProfit = $scope.adminsProfit + $scope.aboutUser.admins[i].count * $scope.aboutUser.admins[i].admin.profit
            }
            if ($scope.adminsProfit > 100) { //максимум - 100%
                $scope.adminsProfit = 100
            }
            //отправляем в $scope
            $scope.$apply();
            console.log(data);
        }
    });

});