import datetime
from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование продукта')
    description = models.TextField(verbose_name='Описание продукта',
                                   help_text='Введите описание продукта',default='отсутствует')
    photo = models.ImageField(upload_to='products/photo', blank=True, null=True, verbose_name='Фото',
                              help_text='Загрузите фото продукта')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, verbose_name='Категория',
                                 help_text='Введите категорию продукта', blank=True, null=True, related_name='products')
    price = models.IntegerField(blank=False, null=False, verbose_name='Цена', help_text='Введите цену продукта')
    created_at = models.DateField(blank=False, null=False, default=datetime.date.today,
                                  verbose_name='Дата создания', help_text='Укажите дату создания')
    updated_at = models.DateField(blank=False, null=False, default=datetime.date.today,
                                  verbose_name='Дата изменения', help_text='Укажите дату изменения')
    published = models.BooleanField(default=False, verbose_name='Опубликовано', help_text='Введите статус публикации')
    # owner = models.ForeignKey(User, verbose_name="Владелец", help_text="Укажите владельца продукта", blank=True,
    #                           null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']
        permissions = [
            ("can_unpublish_product", "can unpublish product"),
        ]


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование категории')
    description = models.TextField(blank=True, null=True, verbose_name='Описание категории',
                                   help_text='Введите описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
