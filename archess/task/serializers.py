from task.models import Task
from rest_framework import serializers
from archess.serializers import UserShortSerializer


class TaskGetSerializer(serializers.ModelSerializer):
    author = UserShortSerializer(many=False)
    class Meta:
        model = Task
        fields = ('id', 'title', 'author', 'start_pos', 'question', 'difficulty', 'likes')


class TaskPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'start_pos', 'question', 'difficulty')

