from django.shortcuts import render

def index(request):
    template_name = 'index.html'
    context = {}
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