from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Scope, ArticleMain


def articles_list(request):
    template = 'articles/news.html'

    articles = Article.objects.order_by('-published_at')
    # for scope in articles:
    #     scope.articlemain_set.order_by('-is_main')
    #     print(scope.articlemain_set.all())
    #     for object in scope.articlemain_set.all():
    #         print(object.is_main)
    #         print(object.scope.topic)
    context = {
        'object_list': articles,
    }
    return render(request, template, context)
