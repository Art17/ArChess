from task.models import Task
from rest_framework import serializers
from archess.serializers import UserShortSerializer


class TaskSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(many=False)
    class Meta:
        model = Task
        fields = ('id', 'title', 'author', 'start_pos', 'question', 'difficulty', 'likes')