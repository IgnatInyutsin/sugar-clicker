main.controller('footer', function ($scope, $http, $location, $cookies) {
    //контроллер страницы footer
    $scope.closeSuccessPassive = function () {
        console.log(document.getElementsByClassName('success-passive')[0])
        document.getElementsByClassName('success-passive')[0].style.display = "none"
    }
    if ($scope.login) {
        let checker = new Api();
        checker.checkSession($cookies.get('session'), $cookies.get('user_id'))
    }
});