from django.shortcuts import render
from rest_framework import viewsets, generics

from education.models import Course, Lesson, Payment
from education.serializers import CourseSerializers, LesonSerializers, PaymentSerializers


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LesonSerializers


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LesonSerializers
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LesonSerializers
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LesonSerializers
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    filterset_fields = ('course__name', 'lesson__name', 'payment_method')
    ordering_fields = ('payment_date',)
