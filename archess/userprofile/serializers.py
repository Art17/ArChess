from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Statistics

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'avatar']


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ['rating', 'games_won', 'games_lost', 'games_drawn']