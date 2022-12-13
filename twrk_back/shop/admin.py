from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'article', 'cost', 'status', 'image')
    list_filter = ('status',)
    search_fields = ('title', 'article')
    empty_value_display = '-пусто-'
