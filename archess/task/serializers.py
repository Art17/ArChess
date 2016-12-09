from task.models import Task
from rest_framework import serializers
from archess.serializers import UserShortSerializer
from django.contrib.auth.models import User

class TaskGetSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(many=False)
    class Meta:
        model = Task
        fields = ('id', 'title', 'author', 'start_pos', 'question', 'difficulty', 'likes')


class TaskPutSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('title', 'author', 'start_pos', 'question', 'difficulty')

