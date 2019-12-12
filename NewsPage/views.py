from django.shortcuts import render
from api.models import BcNews
from django.http import JsonResponse

def index(request):
    news_list = BcNews.objects.all()
    return render(request, 'news_index.html', {'news_list':news_list})

def news_detail(request, path):
    targetnews = BcNews.objects.get(title=path)
    news = dict({'title':targetnews.title, 'author':targetnews.author, 'date':targetnews.date, 'content':targetnews.content})
    return JsonResponse(news)
