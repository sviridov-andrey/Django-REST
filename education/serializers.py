from rest_framework import serializers

from education.models import Course, Leson


class CourseSerializers(serializers.ModelSerializer):
    lesons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

        def get_lesons_count(self, instance):
            return instance.leson_set.count()


class LesonSerializers(serializers.ModelSerializer):

    class Meta:
        model = Leson
        fields = '__all__'
