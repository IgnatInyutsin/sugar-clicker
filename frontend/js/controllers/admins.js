main.controller('admins', function ($scope, $http, $location, $cookies) {
    //контроллер страницы admins
    $scope.$parent.pageName = 'admins';
    //подключаем BackendConnector
    let urls = new BackendConnector();
    //делаем get запроc
    $.ajax({
        url: urls.domain + 'admins/shop/',
        method: 'get',
        datatype: 'application/json',
        success: function (data) {
            $scope.adminsList = data;
            $scope.$apply();
            console.log(data);
        }
    });
});