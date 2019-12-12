from rest_framework import serializers
from .models import UserStates, BcNews

class SteamStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStates
        fields = ['username', 'state', 'game', 'crawltime', 'userurl']

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BcNews
        fields = ['title', 'date', 'author', 'content', 'newsurl']
