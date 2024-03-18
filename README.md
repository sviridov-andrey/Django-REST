# Платформа обучения

## Для работы с проектом необходимо выполнить следующие действия:

- Клонировать репозиторий.
- Активировать виртуальное окружение env/bin/activate.bat
- Установить зависимости pip install -r requirements.txt
- Создать файл .env, заполнить его данными из файла env.sample
- Создать базу данных в PostreSQL CREATE DATABASE django_rest;
- Создать python manage.py makemigration и применить миграции python manage.py migrate
- Создать пользователя командой python manage.py csu
- Установить и запустить Docker Desktop локально (на Windows)
- Собрать образ командой docker-compose build
- Запустить контейнеры командой docker-compose up
- Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению.
