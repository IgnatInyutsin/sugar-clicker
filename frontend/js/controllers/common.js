/**
 Контроллер, выполняющийся при формировании каждой страницы
 */
main.controller('common', function ($scope, $http, $location, $cookies, $timeout) {

    $scope.showUpButton = false; // Кнопка перемотки вверх

    $scope.pageTop = function () { // Функция перемотки вверх
        $("html, body").animate({scrollTop: 0}, 600);
        return false;
    }

    if (document.location.hash == "") document.location.hash = '!/index/'; //если переходят по пустому хэшу то редирект на главную страницу

    //проверка, зашел ли человек в аккаунт
    if (!$cookies.get('session')) {
        $scope.login = false;
    } else {
        $scope.login = true;
    }
});