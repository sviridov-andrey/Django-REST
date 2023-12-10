from django.urls import path

from education.apps import EducationConfig
from rest_framework.routers import DefaultRouter

from education.views import CourseViewSet, LesonCreateAPIView, LesonListAPIView, LesonRetrieveAPIView, \
    LesonUpdateAPIView, LesonDestroyAPIView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'education', CourseViewSet, basename='education')

urlpatterns = [
    path('leson/create/', LesonCreateAPIView.as_view(), name='leson_create'),
    path('leson/', LesonListAPIView.as_view(), name='leson_list'),
    path('leson/<int:pk>/', LesonRetrieveAPIView.as_view(), name='leson_retpieve'),
    path('leson/update/<int:pk>/', LesonUpdateAPIView.as_view(), name='leson_update'),
    path('leson/destroy/<int:pk>/', LesonDestroyAPIView.as_view(), name='leson_destroy'),
    ] + router.urls
