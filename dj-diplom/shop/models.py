from django.db import models
from datetime import datetime
max_length = 20

class Article(models.Model):
    title = models.CharField(max_length='256', null=False, default="", verbose_name='Заголовок')
    sub_title = models.CharField(max_length='256', null=False, default="", verbose_name='Подзаголовок')

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'

    def __str__(self):
        return self.title


class Item(models.Model):
    name =
    image =
    description =
    reviews = models.ForeignKey(Review)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=max_length, verbose_name='Имя')

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, unique=True)
    stars = models.PositiveIntegerField(verbose_name='Рейтинг')
    text = models.CharField(max_length='256', null=False, default="", verbose_name='Текст')
    date = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'


class User
    pass

class Cart
    user = models.ForeignKey(User, unique=True)
    item = models.ManyToManyField(Item)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    class Meta
        verbose_name='Корзина'

class Order
    date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, unique=True)
    item = models.ManyToManyField(Item)
    quantity = models.PositiveIntegerField(default=1)
    is_finished = models.BooleanField