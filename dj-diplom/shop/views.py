from django.shortcuts import render
from .models import Article, Category, Item
from django.core.paginator import Paginator
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import reverse
import urllib
from django.contrib.auth import get_user_model


def index(request):
    template_name = 'index.html'
    articles = Article.objects.order_by('-date_created')

    context = {
        'articles': articles,
    }
    return render(request, template_name, context)

def item_page(request, pk):
    template_name = 'item.html'
    item = Item.objects.get(id=pk)
    context = {
        "item": item,
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
    items_per_page = 3
    items = Item.objects.filter(category__id=pk)
    p = Paginator(items, items_per_page)
    page_number = 1 if request.GET.get('page') == None else int(request.GET.get('page'))
    if p.page(page_number).has_next():
        next_page_url = reverse('category', args=[pk]) + '?' + urllib.parse.urlencode({'page': p.page(page_number).next_page_number()})
    else:
        next_page_url = None
    if p.page(page_number).has_previous():
        prev_page_url = reverse('category', args=[pk]) + '?' + urllib.parse.urlencode(
        {'page': p.page(page_number).previous_page_number()})
    else:
        prev_page_url = None
    context = {
        "items": p.page(page_number),
        "category": Category.objects.get(id=pk).name,
        'current_page': page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }
    return render(request, template_name, context)


# def login(request):
#     auth_views.login(request)
#     return render(request, 'registration/login.html', context)
#
# def logged_out(request):
#     auth_views.logout(request)
#     return render(request, 'registration/logged_out.html', context)

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        print(User)
        form = UserCreationForm(request.POST)
        form.Meta.model = User
        print(form.Meta.model)
        if form.is_valid():
            print('1')
            username = form.cleaned_data.get('username')
            print('2')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            print('3')
            user = User.objects.create_user(username,"",password)
    else:

        form = UserCreationForm()
    context={
        'form': form,
    }
    return render(request, 'registration/signup.html', context)