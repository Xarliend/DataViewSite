from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SteamStateSerializer, NewsSerializer
from .models import UserStates, BcNews

class SteamStatesViewset(viewsets.ModelViewSet):
    queryset = UserStates.objects.all()
    serializer_class = SteamStateSerializer

class NewsViewset(viewsets.ModelViewSet):
    queryset = BcNews.objects.all()
    serializer_class = NewsSerializer
