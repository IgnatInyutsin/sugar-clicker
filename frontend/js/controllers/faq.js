main.controller('faq', function ($scope, $http, $location, $cookies) {
    //контроллер страницы registration
    $scope.$parent.pageName = 'faq';
    if ($scope.login) {
        let checker = new Api();
        checker.checkSession($cookies.get('session'), $cookies.get('user_id'))
    }
});