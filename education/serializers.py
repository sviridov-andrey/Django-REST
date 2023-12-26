from rest_framework import serializers

from education.models import Course, Lesson, Payment, Subscription
from education.validators import VideoValidator


class LessonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoValidator(field='video')]


class CourseSerializers(serializers.ModelSerializer):
    subscribed = serializers.SerializerMethodField()
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializers(source='lesson_set', read_only=True, many=True)

    def get_subscribed(self, instance):
        request = self.context.get('request')
        if request:
            return Subscription.objects.filter(user=request.user, course=instance).exists()
        return False

    class Meta:
        model = Course
        fields = '__all__'

        def get_lessons_count(self, instance):
            return instance.lesson_set.count()


class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
