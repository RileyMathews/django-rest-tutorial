# api/views.py
from rest_framework import viewsets

from todos import models
from . import serializers


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSeralizer