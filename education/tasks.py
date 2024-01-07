from celery import shared_task
from django.core.mail import send_mail
from config import settings
from education.models import Course, Subscription
from users.models import User
import datetime


@shared_task
def check_update_course(pk):
    """Проверка обновления курса"""
    course = Course.objects.get(pk=pk)
    subscriptions = Subscription.objects.filter(course=pk)

    if subscriptions:
        for subscription in subscriptions:
            send_mail(f"Your subscription on site.",
                      f"Привет, {subscription.user}! Курс {course.name} обновлен!",
                      settings.EMAIL_HOST_USER,
                      ["sicklynumb@yandex.ru"],
                      )


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
                    user.save()
            else:
                user.last_login = current_date
                user.save()
