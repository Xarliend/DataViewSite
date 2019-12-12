"""DataView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from api import views as apiviews
from rest_framework import routers
from NewsPage import views as newsviews
from . import views

router = routers.DefaultRouter()
router.register(r'steamstates', apiviews.SteamStatesViewset)
router.register(r'news', apiviews.NewsViewset)

urlpatterns = [
    path('', views.portal),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('news/', newsviews.index),
    re_path(r'^news/(?P<path>.*)$', newsviews.news_detail),
]
