# CRUD Project

### Тестовое задание.
**Задача**: API CRUD пользователей 

Сервер с запущенным решением: > 
http://78.29.38.1:5016/swagger/

Для того, чтобы развернуть данное решение на локальное машине, потребуется осуществить следующие действия: 

**Клонируем репозитория:**

`git clone https://github.com/acecrosser/crud_project.git`

**Переходим в созданную папку проекта:**

`cd crud_project`

**Создаем виртуальное окружение Python:**

`python -m venv env` *(после создения появиться папка env)*

**Активируем виртуальное окружение:**

Windows: `cd env\Scripts\` > `activate`

Linux: `source env/bin/activate`

**Обновляем pip:**

`pip install --upgrade pip`

**Устанавливаем все необходимые зависимости из файла requirements.txt**

`pip install -r requirements.txt`

**Переходим в папку app/ и создаем правила миграци моделей:**

`cd app/` > `python manage.py makemigrations users`

**Делаем миграцию моделей:**

`python manage.py migrate`

**Создаем суперпользователя:**

`python manage.py createsuperuser`

**Запускаем проект:**

`python manage.py runserver`

Переходим на страницу > http://127.0.0.1:8000/swagger/
