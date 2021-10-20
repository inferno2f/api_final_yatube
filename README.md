# Yatube API

В этом репозитории вы сможете найти API, которую можно использовать для блогов, социальных сетей и т.д.


## Реализованный функционал API:

 - Публикации
 - Комментарии
 - Группы
 - Подписки
 
 CRUD фундамент подготовлен для всех вышеупомянутых разделов. Настраивайте пермишены на ваше усмотрение.

## Как развернуть проект у себя локально

 1. Клонируйте проект 
 `git clone <ссылка_проекта_на_гитхаб>`
 
2. Зайдите в папку проекта и создайте виртуальное окружение
`python3 -m venv env`

3. Активируйте вирт окружение и установите все зависимости
`source env/bin/activate`
`pip install -r requirements.txt`


## Документация API

Все доступные эндпойнты, типы запросов и модели вы найдете запустив сервер и перейдя по адресу

    http://127.0.0.1:8000/swagger/

