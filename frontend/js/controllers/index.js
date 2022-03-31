main.controller('index', function ($scope, $http, $location, $cookies) {
    //контроллер страницы index
    $scope.$parent.pageName = 'index';

    // проверяем на действительность сессии
    if ($scope.login) {
        let checker = new Api();
        checker.checkSession($cookies.get('session'), $cookies.get('user_id'))
    }

    //обработка клика по кнопке "стащить пакет"
    $scope.sugarAddClick = function () {
        $scope.sugarClicks++;
    }

    //обработка клика по кнопке "забрать"
    $scope.sugarRemoveClick = function () {
        let urls = new BackendConnector();
        $.ajax({
            url: urls.domain + 'user/list/' + $cookies.get("user_id") + "/",
            method: 'patch',
            datatype: 'application/json',
            data: {session_uuid: $cookies.get("session"), balance: $scope.sugarClicks},
            success: function (data) {
                document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-success fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                    '    <strong>Баланс</strong> В баланс успешно добавлено ' + $scope.sugarClicks + ' пакет(а/ов) сахара' +
                    '\n' +
                    '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                    '</div>');
                $scope.sugarClicks = 0;
                $scope.$apply();
            }
        });
    }

    //обработка клика по кнопке "собрать пассивный доход"
    $scope.collectPassiveIncome = function () {
        let urls = new BackendConnector();
        $.ajax({ //добавляем пассивный доход
            url: urls.domain + 'user/passive_income/' + $cookies.get("user_id") + "/",
            method: 'patch',
            datatype: 'application/json',
            success: function (data) {
                document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-success fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                    '    <strong>Баланс</strong> Пассивный доход собран. В баланс успешно добавлено ' + data.adding + ' пакет(а/ов) сахара' +
                    '\n' +
                    '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                    '</div>');
            }
        });
    }
});