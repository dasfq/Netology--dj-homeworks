from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    ordering = '-published_at'
    articles = Article.objects.prefetch_related('author').defer('published_at').order_by(ordering)
    context = {
        'object_list': articles
    }


    return render(request, template_name, context)
