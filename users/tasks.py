from celery import shared_task
import datetime
from users.models import User


@shared_task
def check_user_activity():
    """Проверка непосещения сайта пользователем более 30 дней"""
    users = User.objects.filter(is_active=True)
    current_date = datetime.datetime.now()

    if users:
        for user in users:
            if user.last_login:
                user_last_login = user.last_login
                if (current_date - user_last_login.date()).days > 30:
                    user.is_active = False
            else:
                user.last_login = current_date

        User.objects.bulk_update(users, ['is_active', 'last_login'])
