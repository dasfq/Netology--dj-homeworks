from django.contrib import admin
from .models import Phone

class PhoneAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phone)