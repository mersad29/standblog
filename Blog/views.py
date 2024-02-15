from django.shortcuts import render, get_object_or_404, redirect
from index.models import Article, Category, Comment
from django.core.paginator import Paginator
from .forms import ContactUsForm

def detail_page(request, slug):
    articles = Article.objects.get(slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=articles, user=request.user, parent_id=parent_id)

    return render(request, 'index/post-details.html', context={'articles': articles})


def articles_page(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 1)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)
    return render(request, 'index/atricles_list.html', context={'articles': objects_list})


def category_articles(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.article_set.all()
    return render(request, 'index/atricles_list.html', context={'articles': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 1)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)
    return render(request, 'index/atricles_list.html', context={'articles': objects_list})


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            return redirect('index:home')
    else:
        form = ContactUsForm()
    return render(request, 'contact.html', {"form": form})

