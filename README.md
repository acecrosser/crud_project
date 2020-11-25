# CRUD Project

### Тестовое задание. 

**Задача** - CRUD проект с токен авторизацией. 

 **Requirements:** Django, Django REST, JWT 

**Создать нового пользователя (Обязательный поля для заполнения `email` и `password`):**

`POST http://78.29.38.1:5016/user/create/`
```
JSON:

{
    "email": "yoursmail@mail.com",
    "password": "yourspassword",
    "first_name": "Name",
    "last_name": "Last Name"
}
```
Ответ сервера: `STAUS 201 Created`
```

{
    "id": 14,
    "email": "yoursmail@mail.com",
    "first_name": "Name",
    "last_name": "Last Name",
    "data_create": "2020-11-25T06:42:16.373942Z"
}
```
**Запросить токен авторизации (Обязательный поля для заполнения `email` и `password`):**

`POST http://78.29.38.1:5016/user/take_token/`
```
JSON:

{
    "email": "yoursmail@mail.com",
    "password": "yourspassword"
}
```
Ответ сервера: `STAUS 200 OK`
```
{
    "name": "Name Last Name",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwidXNlcm5hbWUiOiJ5b3Vyc21haWxAbWFpbC5jb20iLCJleHAiOjE2MDYyODcwOTIsImVtYWlsIjoieW91cnNtYWlsQG1haWwuY29tIn0.PFozxj10yzUpYTZLSIpgs3YhWSL8XLbeNYmn4-iEbvs"
}
```
**Создать пост:**

В заголовке Headers указывается дополнительный параметр `Authorization`, где вписываем наш полученный токен 
`CRUD yourtoken`

`POST http://78.29.38.1:5016/crud/`
```
JSON:

{
    "title": "Your title",
    "body": "body message",
    "user_id": 14
}
```
Ответ сервера: `STAUS 201 Created`
```
{
    "id": 4,
    "title": "Your title",
    "body": "body message",
    "user_id": 14,
    "date": "2020-11-25T06:56:12.292380Z"
}
```

Остальные доступные интерфейсы: 
```
GET http://78.29.38.1:5016/crud/ - Выдаст список всех созданных постов (не требует авторизации)
DELET http://78.29.38.1:5016/crud/id_post - Удалит выбранный пост по его номеру id (авторизация обязательна)
PUT http://78.29.38.1:5016/crud/id_post - Внести изменения в созданный пост (авторизация обязательна)
PUT http://78.29.38.1:5016/user/update - Внести изменения в данные пользователя (авторизация обязательна)
```
