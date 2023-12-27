from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from education.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        """Создание тестового пользователя, курса и урока"""
        self.client = APIClient()
        self.user = User.objects.create(email='user@gmail.com', password='123')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            name='test_course',
            description='test_course',
            owner=self.user,
            preview=None
        )

        self.lesson = Lesson.objects.create(
            name='test_lesson',
            description='test_lesson',
            course=self.course,
            video='http://www.youtube.com/test_lesson',
            owner=self.user,
            preview=None
        )

    def test_create(self):
        """Тестирование создания урока"""
        data = {
            'name': 'test_lesson_2',
            'description': 'test_lesson_2',
            'course': self.course.id,
            'video': 'http://www.youtube.com/test_lesson_2',
            'owner': self.user.id
        }

        response = self.client.post(reverse('education:lesson_create'), data=data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2,
             'name': 'test_lesson_2',
             'preview': None,
             'description': 'test_lesson_2',
             'course': self.course.id,
             'owner': self.user.id,
             'video': 'http://www.youtube.com/test_lesson_2'
             }

        )

    def test_list(self):
        """Тестирование вывода списка уроков"""
        response = self.client.get(reverse('education:lesson_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results': [
                 {'id': self.lesson.id,
                  'name': self.lesson.name,
                  'preview': None,
                  'description': self.lesson.description,
                  'course': self.course.id,
                  'owner': self.user.id,
                  'video': self.lesson.video
                  }
             ]
             }
        )

    def test_retrieve(self):
        """Тестирование вывода одного урока"""
        response = self.client.get(reverse('education:lesson_retrieve', kwargs={'pk': self.lesson.id}))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.lesson.id,
             'name': self.lesson.name,
             'preview': None,
             'description': self.lesson.description,
             'course': self.course.id,
             'owner': self.user.id,
             'video': self.lesson.video
             }
        )

    def test_update(self):
        """Тестирование изменения урока"""
        data = {
            'name': 'test_lesson_upd'
        }

        response = self.client.patch(
            reverse('education:lesson_update', kwargs={'pk': self.lesson.id}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': self.lesson.id,
             'name': 'test_lesson_upd',
             'preview': None,
             'description': self.lesson.description,
             'course': self.course.id,
             'owner': self.user.id,
             'video': self.lesson.video
             }
        )

    def test_delete(self):
        """Тестирование удаления урока"""
        response = self.client.delete(
            reverse('education:lesson_destroy', kwargs={'pk': self.lesson.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

# class SubscriptionTestCase(APITestCase):
#
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(email='user@test.com', password='test')
#         self.client.force_authenticate(user=self.user)
#
#         self.course = Course.objects.create(
#             name='test_course',
#             description='test_course',
#             owner=self.user
#         )
#
#     def test_create(self):
#         """Тестирование создания подписки"""
#         subscription = {
#             "user": self.user.id,
#             "course": self.course.id
#         }
#
#         response = self.client.post(
#             reverse('courses:sub_create', kwargs={'pk': self.course.id}),
#             data=subscription
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#     def test_delete(self):
#         """Тестирование удаления подписки"""
#
#         course = Subscription.objects.create(
#             user=self.user,
#             course=self.course
#         )
#
#         response = self.client.delete(
#             reverse('courses:sub_delete', kwargs={'pk': course.id})
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_204_NO_CONTENT
#         )
