from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Product)  # Регистрируем модель
class ProductAdmin(admin.ModelAdmin):
    # Настраиваем поля, которые будем выводить в админке
    list_display = ('id', 'name', 'price','category')
    # По чему будем делать фильтрацию
    list_filter = ('category',)
    # По чему у нас будет поиск
    search_fields = ('name', 'description')


@admin.register(Category)  # Регистрируем модель
class CategoryAdmin(admin.ModelAdmin):
    # Настраиваем поля, которые будем выводить в админке
    list_display = ('id', 'name',)
