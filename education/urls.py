from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentViewSet

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'education', CourseViewSet, basename='education')
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('leson/create/', LessonCreateAPIView.as_view(), name='leson_create'),
    path('leson/', LessonListAPIView.as_view(), name='leson_list'),
    path('leson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='leson_retpieve'),
    path('leson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='leson_update'),
    path('leson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='leson_destroy'),
    ] + router.urls
