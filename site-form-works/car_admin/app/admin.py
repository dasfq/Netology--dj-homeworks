from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm




class CarAdmin(admin.ModelAdmin):
# Какие поля отображать на странице редактирования:
    list_display  = ('brand', 'model', 'review_count')
# Появится строка поиска по этим полям:
    search_fields = ['brand', 'model']
# Добавляет новое поле, которого нет в модели. Можно вынести за класс, тогда в list_display будет без кавычек.
    def review_count(self, obj):
        rev_count = obj.review_set.count()
        return rev_count
# Красивое название для добавленного столбца.
    review_count.short_description = 'Кол-во обзоров'

# Сортировка по полю id.
    ordering = ('id',)

# Справа появится фильтр по этим полям:
    list_filter = ['brand', 'model']


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm

    list_display = ('car', 'title')
    search_fields = ['car', 'title']
    ordering = ('id',)
    list_filter = ['car', 'title']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
