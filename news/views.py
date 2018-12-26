from django.shortcuts import render
from .models import Column, Article


def index(request):
    columns = Column.objects.all()
    context = {'columns': columns}
    return render(request, 'news/index.html', context)


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    context = {'column': column}
    return render(request, 'news/column.html', context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'news/article.html', {'article': article})