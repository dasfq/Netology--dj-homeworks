from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, ArticleMain, Scope
from django.forms.models import BaseInlineFormSet



class ArticleMainInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_marked = 0
        for form in self.forms:
            if is_marked > 1:
                raise ValidationError('Отметьте главным только одно поле')
            if form.cleaned_data.get('is_main') == True:
                is_marked += 1
        if is_marked == 0:
            raise ValidationError('Нужно отметить главное поле')
        return super().clean()

class ArticleMainInline(admin.TabularInline):
    model = ArticleMain
    formset = ArticleMainInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleMainInline]
    pass

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass


