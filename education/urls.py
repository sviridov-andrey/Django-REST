from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentViewSet, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'education', CourseViewSet, basename='education')
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
    path('subscribe/<int:course_pk>/create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscribe/<int:pk>/delete/', SubscriptionDestroyAPIView.as_view(), name='subscription_delete'),
    ] + router.urls
