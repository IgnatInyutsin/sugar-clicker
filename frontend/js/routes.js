//создаем модуль main (подключается в index.html)
var main = angular.module("main", ['ngRoute', 'ngCookies']);

main.config(function ($routeProvider) {
    $routeProvider.when("/index/", {
        controller: "index",
        templateUrl: "views/controllers/index.html"
    });
    $routeProvider.when("/registration/", {
        controller: "registration",
        templateUrl: "views/controllers/registration.html"
    });
    $routeProvider.when("/my_profile/", {
        controller: "profile",
        templateUrl: "views/controllers/profile.html"
    });
    $routeProvider.when("/rating/", {
        controller: "rating",
        templateUrl: "views/controllers/rating.html"
    });
    $routeProvider.when("/faq/", {
        controller: "faq",
        templateUrl: "views/controllers/faq.html"
    });
    $routeProvider.when("/shop/providers/", {
        controller: "providers",
        templateUrl: "views/controllers/providers.html"
    });
    $routeProvider.when("/shop/admins/", {
        controller: "admins",
        templateUrl: "views/controllers/admins.html"
    });
});