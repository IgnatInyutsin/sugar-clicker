main.controller('admins', function ($scope, $http, $location, $cookies) {
    //контроллер страницы admins
    $scope.$parent.pageName = 'admins';
    //подключаем BackendConnector
    let urls = new BackendConnector();
    // проверяем на действительность сессии
    if ($scope.login) {
        let checker = new Api();
        checker.checkSession($cookies.get('session'), $cookies.get('user_id'))
    }

    //делаем get запроcы
    $.ajax({ // достаем наш баланс
        url: urls.domain + "user/list/" + $cookies.get("user_id") + "/",
        method: 'get',
        datatype: 'application/json',
        success: function (data) {
            $scope.balance = data.balance;
            $scope.$apply();
        }
    });

    $.ajax({ //достаем список админов
        url: urls.domain + 'admin/shop/',
        method: 'get',
        datatype: 'application/json',
        success: function (data) {
            $scope.adminsList = data;
            $scope.$apply();
            console.log(data);
        }
    });

    //обработка нажатия на кнопку покупки
    $scope.buyAdmin = function (id) {
        //проверяем, заполнена ли форма к-ва штук
        if (document.getElementById("cost" + id).value == '') {
            document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                '    <strong>Ошибка количества</strong> Введите количество штук \n' +
                '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                '</div>');
            return undefined;
        }

        //отправляем запрос на добавление
        $.ajax({ //достаем список админов
            url: urls.domain + 'admin/group/',
            method: 'post',
            datatype: 'application/json',
            data: {'user.session_uuid': $cookies.get('session'), 'count': Number(document.getElementById("cost" + id).value), 'admin.id': id},
            success: function (data) {
                console.log(data)
                document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-success fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                    '    Вы успешно преобрели ' + document.getElementById("cost" + id).value +  ' администратор(а/ов) \n' +
                    '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                    '</div>');

                document.getElementById('cost' + id).value = ''

                $.ajax({ // достаем наш баланс
                    url: urls.domain + "user/list/" + $cookies.get("user_id") + "/",
                    method: 'get',
                    datatype: 'application/json',
                    success: function (data) {
                        $scope.balance = data.balance;
                        $scope.$apply();
                    }
                });
            },
            error: function (xhr) {
                if (xhr.responseJSON[0].code == 'SMALL_BALANCE') {
                    document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                        '    <strong>Ошибка баланса</strong> Недостаточно денег для покупки! \n' +
                        '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                        '</div>');
                }
            }
        });
    }
});