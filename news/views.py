from django.shortcuts import render
from news.models import news

# Create your views here.
def index(request):
    all_news = news.objects.all()
    return render(request,'news/index.html',{'news':all_news})

def detail(request,id):
    current_news = news.objects.filter(newsId=id)
    if len(current_news):
        current_news = current_news[0]
    return render(request, 'news/news.html',{'news':current_news})