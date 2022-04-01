main.controller('header', function ($scope, $http, $location, $cookies) {
    //контроллер страницы header

    //добавляем данные о user_id пользователя
    if ($scope.login) {
        let urls = new BackendConnector();
        $scope.userID = $cookies.get("user_id")
        $.ajax({
            url: urls.domain + 'user/list/' + $cookies.get('user_id') + "/",
            method: 'get',
            datatype: 'application/json',
            async: false,
            success: function (data) {
                $scope.userName = data.name
                $scope.balance = data.balance
            }
        });
        // данные для строки баланса
        $scope.messageForUser = "Баланс " + $scope.userName + ": " + $scope.balance;
        // делаем их обновляемыми
        setInterval(function () {
            $.ajax({
                url: urls.domain + 'user/list/' + $cookies.get('user_id') + "/",
                method: 'get',
                datatype: 'application/json',
                async: false,
                success: function (data) {
                    $scope.userName = data.name
                    $scope.balance = data.balance
                }
            });
            $scope.messageForUser = "Баланс " + $scope.userName + ": " + $scope.balance;
            $scope.$apply();
        }, 5000);
    } else {
        $scope.messageForUser = "Режим гостя, войдите в аккаунт";
    }

    // проверка заполненности полей входа
    if (!$scope.login) {
        setInterval(function () {
            if (document.getElementById("login_email").value == '') {
                document.getElementById("login-but").disabled = true
            } else if (document.getElementById("login_password").value == '') {
                document.getElementById("login-but").disabled = true
            } else {
                document.getElementById("login-but").disabled = false
            }

        }, 300)
    }

    //обработка клику по кнопке выхода
    $scope.logoutClick = function () {
        $cookies.remove("session");
        location.hash = "!/faq/"
        location.reload();
    }

    // обработка клика по кнопке входа
    $scope.loginClick = function () {
        let api = new Api();
        let urls = new BackendConnector();

        let email = document.getElementById("login_email").value;
        let pass_cache = api.SHA256(document.getElementById("login_password").value);
        var uuid = api.uuidv4();

        $.ajax({
            url: urls.domain + 'user/login/',
            method: 'post',
            datatype: 'application/json',
            data: {email: email, pass_cache: pass_cache, session_uuid: uuid},
            success: function (data) {
                // в успешном случае добавляем кук сессии и обновляемся
                $cookies.put("user_id", data.user_id)
                $cookies.put("session", uuid);
                location.hash = "!/index/"
                location.reload();
            },
            error: function (xhr) {
                console.log(xhr);
                try {
                    if (xhr.responseJSON[0].code == "MISSING_IN_DB_EMAIL") {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    Данный Email не зарегистрирован \n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>')
                    }
                } catch (e) {}

                try {
                    if (xhr.responseJSON.email[0] == 'Enter a valid email address.') {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    Пожалуйста, введите корректный Email \n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>');
                    }
                } catch (e) {}

                try {
                    if (xhr.responseJSON[0].code == "WRONG_PASSWORD") {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    <strong>Ошибка пароля</strong> Неверный пароль \n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>');
                    }
                } catch (e) {}

                try {
                    if (xhr.responseJSON[0].code == 'ACCOUNT_NOT_ACTIVATED') {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    ' +
                            'Аккаунт не активирован. Проверьте свою почту. \n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>');
                    }
                } catch (e) {}
            }
        });
    }
});