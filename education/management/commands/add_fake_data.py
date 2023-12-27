from django.core.management.base import BaseCommand
from education.models import Payment, Lesson, Course
from faker import Faker
import random
from decimal import Decimal
from users.models import User

fake = Faker()


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        User.objects.exclude(email='sicklynumb@yandex.ru').delete()
        Payment.objects.all().delete()
        Lesson.objects.all().delete()
        Course.objects.all().delete()

        users = []
        for i in range(4):
            email = f'user_{i+1}@mail.ru'
            password = '1'
            phone = fake.numerify()
            city = fake.city()
            country = fake.country()
            user = User.objects.create(email=email, password=password, phone=phone, city=city, country=country)
            user.set_password(user.password)
            user.save()
            users.append(user)
        #
        # for user in self.User.objects.all():
        #     user.set_password(user.password)
        #     user.save()

        courses = []
        for _ in range(3):
            course = Course.objects.create(
                name=fake.word(),
                description=fake.text(),
            )
            courses.append(course)

        lessons = []
        for _ in range(9):
            lesson = Lesson.objects.create(
                name=fake.word(),
                description=fake.text(),
                course=random.choice(courses),
            )
            lessons.append(lesson)

        payments = []
        for _ in range(12):
            user = random.choice(users)
            payment_date = fake.date_between(start_date='-60d', end_date='today')
            summ = Decimal(random.uniform(100, 1000))
            payment_method = random.choice(['cash', 'transfer'])

            is_course = random.choice([True, False])
            course_lesson = random.choice(courses) if is_course else random.choice(lessons)

            payment = Payment.objects.create(
                user=user,
                payment_date=payment_date,
                paid_course=course_lesson if is_course else None,
                paid_lesson=course_lesson if not is_course else None,
                summ=summ,
                payment_method=payment_method,
            )
            payments.append(payment)
