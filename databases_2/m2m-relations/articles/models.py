from django.db import models

class Scope(models.Model):
    topic = models.CharField(max_length=256, verbose_name='Тема')
    class Meta:
        ordering = ['topic']
        verbose_name = "Тема"
        verbose_name_plural = 'Темы'
    def __str__(self):
        return self.topic

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Scope, through='ArticleMain')
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    def __str__(self):
        return self.title

class ArticleMain(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Главный раздел')

    class Meta:
        ordering = ['-is_main']