from django.shortcuts import render
from .models import Article, Category

def index(request):
    template_name = 'index.html'
    articles = Article.objects.order_by('-date_created')
# не пойму почему print выдаёт None
    print(articles[0].category.item_set.all())
    context = {
        'articles': articles,
    }
    return render(request, template_name, context)

def phone_page(request):
    template_name = 'phone_page.html'
    context = {}
    return render(request, template_name, context)

def cart(request):
    template_name = 'cart.html'
    context = {}
    return render(request, template_name, context)

def empty_section(request):
    template_name = 'empty_section.html'
    context = {}
    return render(request, template_name, context)

def login(request):
    template_name = 'login.html'
    context = {}
    return render(request, template_name, context)

def smartphones(request):
    template_name = 'smartphones.html'
    context = {}
    return render(request, template_name, context)