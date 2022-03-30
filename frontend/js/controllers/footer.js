main.controller('footer', function ($scope, $http, $location, $cookies) {
    //контроллер страницы footer
    $scope.closeSuccessPassive = function () {
        console.log(document.getElementsByClassName('success-passive')[0])
        document.getElementsByClassName('success-passive')[0].style.display = "none"
    }

});