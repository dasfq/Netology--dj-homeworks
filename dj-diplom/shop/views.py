from django.shortcuts import render
from .models import Article, Category, Item
from django.core.paginator import Paginator

def index(request):
    template_name = 'index.html'
    articles = Article.objects.order_by('-date_created')

    context = {
        'articles': articles,
    }
    return render(request, template_name, context)

def item_page(request):
    template_name = 'item.html'
    context = {}
    return render(request, template_name, context)

def add_cart(request):
    if request.method == 'POST':
        pass

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

def category_view(request, pk):
    template_name = 'category.html'
    items = Item.objects.filter(category__id=pk)
    context = {
        "items": items,
        "category": Category.objects.get(id=pk).name
    }
    return render(request, template_name, context)