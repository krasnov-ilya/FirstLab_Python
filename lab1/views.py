from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from articles.models import Article


def index(request):
    latest = Article.objects.latest('pub_date')
    return render(request, "index.html", {"article": latest})


def stats(request):
    articles = Article.objects.all()
    return render(request, "stats.html", {"articles": articles})


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.increment_views()
    article.save()
    return render(request, "detail.html", {"article": article})


def articles(request):
    articles = Article.objects.all()
    return render(request, "blog.html", {"articles": articles})


def about(request):
    return render(request, "about.html")
