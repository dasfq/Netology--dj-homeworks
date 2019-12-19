from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Phone


def index(request):
    return redirect('https://www.apelcinema.com/')

def show_catalog(request):
    template = 'catalog.html'
    sort_by = request.GET.get('sorting')
    if not sort_by:
        sort_by = 'name'
    phones_list = Phone.objects.order_by(sort_by)
    print(phones_list)
    context = {
        'items': phones_list
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    item = Phone.objects.get(slug=slug)
    context = {
        'item': item
    }
    return render(request, template, context)