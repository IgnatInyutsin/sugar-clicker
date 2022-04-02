# SUGAR CLICKER
## Об игре
Sugar Clicker - веб-игра с открытым исходным кодом на актуальную в наше время тему. Она отвлекает от недостатка сахара, потому что сахара здесь хоть отбавляй!
## Запуск веб-приложения
Перед запуском веб-приложения обязательно прочтите раздел ["Настройка Django"](#настройка-django)
Для запуска веб-приложения необходимо установить docker и docker-compose.
Порядок действий:
- Перейдите в папку docker/sugar-clicker_instances
  ```bash 
  cd docker/sugar-clicker_instances
  ```
- Скопируйте содержимое файла .env.sample в новосозданный файл .env
  ```bash
  cp .env.sample .env
  ```
- Отредактируйте файл .env под себя, подробнее можно [здесь](#редактирование-env)
- Соберите проект
  ```bash
  ./build
  ``` 
  или
  ```bash
  docker-compose build
  ```
- Запуск осуществляется с помощью
  ```bash
  ./start
  ```
  или
  ```bash
  docker-compose up -d
  ```
- Остановка осуществляется с помощью
  ```bash
  ./stop
  ```
  или
  ```bash
  docker-compose down
   ```
## Редактирование .env
С помощью граммотной настройки переменного накружения вы сможете запустить проект в удобном месте на вашем компьютере. Рассмотрим, за что отвечае каждая переменная
```NETWORK=172.100.1.49/24```
Укажите здесь сеть, по которой будут взаимодействовать docker-контейнеры. Формат - IPv4/24
    
    DJANGO_PORT=82
    WEBSERVER_PORT=80
    SWAGGER_PORT=83
 Укажите здесь, на каких внешних портах вашего компьютера запускать какие приложение. Формат - строго числовой
 
    DB_NAME=sugar_db
    DB_PORT=5432
    DB_USER=admin
    DB_PASS=TESTPASS888
 Здесь указываются настройки для базы данных. После запуска ./build автоматически будет создана база данных с указанным именем на указанном порте с указанным пользователем, имеющий все привелегии
 
    DJANGO_SECRETKEY=foobar
    DJANGO_DEBUG=1
    DJANGO_LOGGING_LEVEL=INFO
    DJANGO_REQUEST_LOGGING_LEVEL=DEBUG
  Здесь укажите настройки DJANGO. DJANGO_SECRETKEY отвечает за заполнение SECRET_KEY в backend/djangoProject/settings.py. Сделайте его наиболее сложным, чтобы защитить свое приложение. DJANGO_DEBUG, если значение установлено 1, включит режим DEBUG у DJANGO. Если вы планируете его держать в публичном доступе, лучше установить 0, которое отключит режим DEBUG.
  DJANGO_LOGGING_LEVEL и DJANGO_REQUEST_LOGGING_LEVEL принимают значения: DEBUG, INFO, WARNING, ERROR, FATAL. Подробнее про уровни логгирования вы можете почитать [в официальной документации](https://docs.djangoproject.com/en/4.0/topics/logging/#loggers). DJANGO_LOGGING_LEVEL отвечает за логгирование самим DJANGO, а DJANGO_REQUEST_LOGGING_LEVEL за логгирование HTTP/HTTPS запросов.
 
    SMTP_HOST=smtp.yandex.ru
    SMTP_PORT=465
    SMTP_USE_SSL=1
    
    EMAIL=you_email@yandex.ru
    EMAIL_PASSWORD=you_password
  Данное приложение использует почтовый smtp сервер для аутентификации по почте. Укажите здесь актуальные данные smtp сервера. Поле SMTP_USE_SSL принимает значения 0, если шифрования нет и значение 1, если шифрование есть

## Настройка Django
Перед запуском контейнера для логгирования создайте два файла в backend/djangoProject/logs/
- django.log
- request.log

После запуска контейнера миграция осуществляется, но в каком либо случае, чтобы их осуществить, используйте скрипты внутри папки backend
- Перейдите в папку backend
  ```bash
  cd backend/
  ```
- Запустите файл make_migrations
  ```bash
  ./make_migrations
  ```
Так же таблицы Admin и Provider по умолчанию не заполнены, чтобы заполнить, примените команду
  ```bash
  ./load_all_admins_and_providers
   ```
Чтобы создать суперпользователя или осуществить любое другое действие в командной строке в контейнере backend, запустите файл
  ```bash
  ./open_bash
  ```
Все конфиги написаны с использованием стандартных команд docker-compose, поэтому вы можете осуществлять эти действия, используя их

## Настройка подключения к REST.API фронтэнд частью
Перейдите в файл с
классом для подключения к REST
Путь: ```frontend/js/classes/BackendConnector.js```
Измените строку 
```js
this.domain = "https://localhost:82/api/"
``` 
В переменную this.domain напишите ваш адрес REST.api, не забудьте добавить путь api

