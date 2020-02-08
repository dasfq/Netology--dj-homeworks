"""diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop.views import index, cart, empty_section, item_page, category_view, signup, add_to_cart
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('item/<int:pk>/', item_page, name='item_page'),
    path('cart/add/<int:pk>', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('empty_section/', empty_section, name='empty_section'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name="logged_out"),
    path('signup/', signup, name="signup"),
    path('category/<int:pk>/', category_view, name='category'),
    path('admin/', admin.site.urls),
]
