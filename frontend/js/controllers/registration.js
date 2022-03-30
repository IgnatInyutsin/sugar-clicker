main.controller('registration', function ($scope, $http, $location, $cookies) {
    //контроллер страницы registration
    $scope.$parent.pageName = 'registration';

    setInterval(function () { // Проверка заполнения полей
        if (document.getElementById('nickname').value != '') {
            if (document.getElementById('email').value != '') {
                if (document.getElementById('password1').value != '') {
                    if (document.getElementById('password2').value != '') {
                        if (document.getElementById('password2').value == document.getElementById('password1').value) {
                            document.getElementById("reg-btn").disabled = false;
                        }
                    }
                }
            }
        }

        if (document.getElementById('nickname').value == '') {
            document.getElementById("reg-btn").disabled = true;
        }
        if (document.getElementById('email').value == '') {
            document.getElementById("reg-btn").disabled = true;
        }
        if (document.getElementById('password1').value == '') {
            document.getElementById("reg-btn").disabled = true;
        }
        if (document.getElementById('password2').value == '') {
            document.getElementById("reg-btn").disabled = true;
        }
        if (document.getElementById('password2').value != document.getElementById('password1').value) {
            document.getElementById("reg-btn").disabled = true;
        }
    }, 300)

    // событие по нажатию на кнопку
    $scope.clickRegButtion = function () {
        let api = new Api();
        let urls = new BackendConnector();

        let nickname = document.getElementById("nickname").value;
        let email = document.getElementById("email").value;
        let pass_cache = api.SHA256(document.getElementById("password1").value);
        var uuid = api.uuidv4();

        $.ajax({
            url: urls.domain + 'user/list/',
            method: 'post',
            datatype: 'application/json',
            data: {name: nickname, email: email, pass_cache: pass_cache, session_uuid: uuid},
            success: function (data) {
                //в случае успеха - редирект и перезагрузка, срабатывает проверка на вход модуля common
                $cookies.put('user_id', data.id)
                $cookies.put('session', uuid)
                document.location.hash = "";
                location.reload();
            },
            error: function (xhr) {
                console.log(xhr)
                // Обработчики ошибок почты
                if (xhr.responseJSON.email != undefined) {
                    if (xhr.responseJSON.email[0] == "Enter a valid email address.") {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    <strong>Ошибка почты</strong> Введите настоящую почту\n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>');
                    }
                    if (xhr.responseJSON.email[0] == "Enter a valid email address.") {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    <strong>Ошибка почты</strong> Введите настоящую почту\n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>');
                    }
                    if (xhr.responseJSON.email[0] == 'user with this email already exists.') {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    <strong>Ошибка почты</strong> Данный адрес уже занят, введите уникальный\n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>');
                    }
                }
                // Обработчик ошибки имени
                if (xhr.responseJSON.name != undefined) {
                    if (xhr.responseJSON.name[0] == "user with this name already exists.") {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    <strong>Ошибка имени</strong> Это имя уже занято, введите уникальное\n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>');
                    } else {
                        document.querySelector("footer").insertAdjacentHTML('afterbegin', '<div class="alert alert-danger fade show" role="alert" style="position: fixed; left: 0; bottom: 0; width: 100%; display: flex; justify-content: space-between">\n' +
                            '    <strong>Ошибка имени</strong> Слишком длинное имя, макс. 256 символов /n' +
                            '    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>\n' +
                            '</div>');
                    }
                }
            }
        })
    }
});