from django.contrib.auth.models import User
from rest_framework import serializers
from userprofile.serializers import ProfileSerializer, StatisticsSerializer


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False)
    statistics = StatisticsSerializer(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile', 'statistics')


class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')