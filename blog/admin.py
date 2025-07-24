from django.contrib import admin

from blog.models import Article


@admin.register(Article)  # Регистрируем модель
class BlogAdmin(admin.ModelAdmin):
    # Настраиваем поля, которые будем выводить в админке
    list_display = ('id', 'title', 'content','published')
    # По чему будем делать фильтрацию
    list_filter = ('title',)
    # По чему у нас будет поиск
    search_fields = ('title', 'content')
