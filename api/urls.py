# api/urls.py
from django.urls import path

from .views import TodoViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todos', TodoViewSet, base_name='todos')
router.register('users', UserViewSet, base_name='users')
urlpatterns = router.urls