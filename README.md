# Django REST + Docker 

## Для работы с проектом необходимо выполнить следующие действия:

- Клонировать репозиторий.
- Активировать виртуальное окружение env/bin/activate.bat
- Установить зависимости pip install -r requirements.txt
- Создать файл .env, заполнить его данными из файла env.sample
- Создать базу данных в PostreSQL CREATE DATABASE django_rest
- Создать python manage.py makemigrate и применить миграции python manage.py migrate
- Создать пользователя командой python manage.py csu
- Создать пользователя командой python manage.py user_create
- Установить и запустить Redis локально (на Windows)
- В терминале набрать команду celery -A config worker -l info --pool=solo
- В терминале набрать команду celery -A config beat -l info -S django
- Запустить проект python manage.py runserver
- Откройте браузер и перейдите по адресу http://127.0.0.1:8000 для доступа к приложению.


  
# Команды:
Применить миграции docker-compose exec app python manage.py migrate  
Собрать образ командой docker-compose build
Запустить контейнеры командой docker-compose up
Либо docker-compose up -d --build

