from rest_framework.routers import DefaultRouter
from .views import FeedbackFormViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'blog', FeedbackFormViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]