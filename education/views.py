from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from education.models import Course, Lesson, Payment, Subscription
from education.permissions import ModerateOrOwner
from education.serializers import CourseSerializers, LessonSerializers, PaymentSerializers, SubscriptionSerializer


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


class SubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [ModerateOrOwner]

    def create(self, request, *args, **kwargs):
        course_pk = self.kwargs.get('course_pk')

        serializer = self.get_serializer(data={'user': request.user.pk, 'course': course_pk})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'Вы подписаны на курс.'}, status=status.HTTP_201_CREATED)


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [ModerateOrOwner]