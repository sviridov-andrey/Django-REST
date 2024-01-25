from celery import shared_task
import datetime

from dateutil.relativedelta import relativedelta

from users.models import User


@shared_task
def check_user_activity():
    """Проверка непосещения сайта пользователем более 30 дней"""

    current_date = datetime.datetime.now()
    month_ago = current_date - relativedelta(months=1)
    users = User.objects.filter(is_active=True, last_login__lte=month_ago)

    if users:
        for user in users:
            user.is_active = False

    User.objects.bulk_update(users, ['is_active'])
