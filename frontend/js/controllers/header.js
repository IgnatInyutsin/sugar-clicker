main.controller('header', function ($scope, $http, $location, $cookies) {
    //контроллер страницы header

    //обработка клику по кнопке выхода
    $scope.logoutClick = function () {
        $cookies.remove("session");
        location.reload();
    }
});