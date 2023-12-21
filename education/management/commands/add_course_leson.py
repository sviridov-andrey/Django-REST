from django.core.management import BaseCommand
from education.models import Course, Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):

        try:
            Course.objects.all().delete()
        except:
            pass

        course_list = [
            {'name': 'course 1',
             'description': 'course 1',
             },
            {'name': 'course 2',
             'description': 'course 2',
             },
            {'name': 'course 3',
             'description': 'course 3',
             },
            {'name': 'course 4',
             'description': 'course 4',
             },
            {'name': 'course 5',
             'description': 'course 5',
             },
        ]

        lesson_list = [
            {'name': 'lesson 1',
             'description': 'lesson 1',
             },
            {'name': 'lesson 2',
             'description': 'lesson 2',
             },
            {'name': 'lesson 3',
             'description': 'lesson 3',
             },
            {'name': 'lesson 4',
             'description': 'lesson 4',
             },
            {'name': 'lesson 5',
             'description': 'lesson 5',
             },
        ]

        courses = []
        lessons = []

        for course in course_list:
            courses = courses.append(course)

        for lesson in lesson_list:
            lessons = lessons.append(lesson)

        Course.objects.bulk_create(courses)
        Lesson.objects.bulk_create(lessons)
