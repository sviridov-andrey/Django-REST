from django.shortcuts import render
from rest_framework import viewsets, generics

from education.models import Course, Leson
from education.serializers import CourseSerializers, LesonSerializers


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()


class LesonCreateAPIView(generics.CreateAPIView):
    serializer_class = LesonSerializers


class LesonListAPIView(generics.ListAPIView):
    serializer_class = LesonSerializers
    queryset = Leson.objects.all()


class LesonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LesonSerializers
    queryset = Leson.objects.all()


class LesonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LesonSerializers
    queryset = Leson.objects.all()


class LesonDestroyAPIView(generics.DestroyAPIView):
    queryset = Leson.objects.all()
