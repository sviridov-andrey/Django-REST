from django.core.management import BaseCommand

from education.models import Payment, Course, Lesson
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        try:
            Payment.objects.all().delete()
        except:
            pass

        payment_list = [
            {'user': User.objects.get(email='user1@mail.com'),
             'purchased_item': Course.objects.get(name='course 1'),
             'summ': 2000,
             'payment_method': 'transfer',
             },
        ]

        payments = []

        for payment in payment_list:
            payments = payments.append(payment)

        Payment.objects.bulk_create(payments)