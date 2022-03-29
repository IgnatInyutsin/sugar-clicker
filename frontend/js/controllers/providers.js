main.controller('providers', function ($scope, $http, $location, $cookies) {
    //контроллер страницы providers
    $scope.$parent.pageName = 'providers';
    //подключаем BackendConnector
    let urls = new BackendConnector();
    //делаем get запроc
    $.ajax({
        url: urls.domain + 'providers/',
        method: 'get',
        datatype: 'application/json',
        success: function (data) {
            $scope.providersList = data;
            $scope.$apply();
            console.log(data);
        }
    });
});