from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
max_length = 20


class Category(models.Model):
    name = models.CharField(max_length=max_length, verbose_name='Имя')

    class Meta:
        verbose_name='Категория товара'
        verbose_name_plural='Категории товара'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, default="", verbose_name='Заголовок')
    sub_title = models.CharField(max_length=200, null=False, default="", verbose_name='Подзаголовок')
    date_created = models.DateTimeField(auto_now_add=False, verbose_name='Дата создания')
    category = models.ForeignKey(Category, default="", null=False, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'

    def __str__(self):
        return self.title


class User(AbstractUser):
    pass


class Item(models.Model):
    name = models.CharField(max_length=max_length, verbose_name='Наименование')
    image = models.ImageField(max_length=max_length, verbose_name='Картинка')
    description = models.CharField(max_length=max_length, verbose_name='Описание')
    category = models.ManyToManyField(Category, verbose_name='Категория товаров')

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    stars = models.PositiveIntegerField(verbose_name='Рейтинг')
    text = models.CharField(max_length=200, null=False, default="", verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=False, verbose_name='Дата отзыва')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, verbose_name="Отзывы")

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, verbose_name="Пользователь")
    item = models.ManyToManyField(Item, through="CartInfo", verbose_name='Товар')

    class Meta:
        verbose_name='Корзина'
        verbose_name_plural='Корзины'


class CartInfo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta:
        verbose_name='Корзина-инфо'


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    item = models.ManyToManyField(Item, through='OrderInfo')


class OrderInfo(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_finished = models.BooleanField