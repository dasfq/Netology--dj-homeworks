from django.shortcuts import render
from .models import Article, Category, Item
from django.core.paginator import Paginator
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm


categories = Category.objects.all()

def index(request):
    template_name = 'index.html'
    articles = Article.objects.order_by('-date_created')

    context = {
        'articles': articles,
        "categories": categories,
    }
    return render(request, template_name, context)

def item_page(request, pk):
    template_name = 'item.html'
    item = Item.objects.get(id=pk)
    context = {
        "item": item,
        "categories": categories,
    }
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

def category_view(request, pk):
    template_name = 'category.html'
    items = Item.objects.filter(category__id=pk)
    context = {
        "items": items,
        "category": Category.objects.get(id=pk).name,
        "categories": categories,
    }
    return render(request, template_name, context)


class login(auth_views.LoginView):
    extra_context = {
        "categories": categories,
    }

def logged_out(request):
    auth_views.logout(request)
    context = {
        "categories": categories,
    }
    return render(request, 'registration/logged_out.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = User.objects.create_user(username,"",password)
    else:
        form = UserCreationForm()
    context={
        'form': form,
        'categories': categories,
    }
    return render(request, 'registration/signup.html', context)