from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from education.models import Course, Lesson, Payment
from education.permissions import ModerateOrOwner
from education.serializers import CourseSerializers, LessonSerializers, PaymentSerializers


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializers
    queryset = Course.objects.all()
    permission_classes = [ModerateOrOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializers
    permission_classes = [ModerateOrOwner]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [ModerateOrOwner]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [ModerateOrOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializers
    queryset = Lesson.objects.all()
    permission_classes = [ModerateOrOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [ModerateOrOwner]


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    filterset_fields = ('course__name', 'lesson__name', 'payment_method')
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated]
