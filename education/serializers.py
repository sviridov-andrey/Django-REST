from rest_framework import serializers

from education.models import Course, Lesson, Payment


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializers(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializers(source='lesson_set', read_only=True, many=True )

    class Meta:
        model = Course
        fields = '__all__'

        def get_lessons_count(self, instance):
            return instance.leson_set.count()


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
