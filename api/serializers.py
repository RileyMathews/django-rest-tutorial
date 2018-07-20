# api/serializers.py
from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Todo

class UserSeralizer(serializers.ModelSerializer):
    todos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'gamertag',
            'password',
            'todos',
        )
        model = models.User