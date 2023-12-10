from rest_framework import serializers

from education.models import Course, Leson


class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class LesonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Leson
        fields = '__all__'
