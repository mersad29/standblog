from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()
    # sarticles = Article.starManager.all()
    # recent_articles = Article.objects.all().order_by('-time_created')
    return render(request, 'index/index.html', context={"articles": articles})


