from django.contrib import admin

from education.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'owner',)
    list_filter = ('name', 'owner',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'course', 'owner',)
    list_filter = ('name', 'description', 'course', 'owner',)
