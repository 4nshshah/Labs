from django.contrib import admin

# Register your models here.
from .models import *
class webappCategoryAdmin(admin.ModelAdmin):
    list_display =("Category",)

class webappPageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category'
    )
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Human)