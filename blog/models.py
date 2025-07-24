from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок')
    content = models.TextField(blank=False, null=False, verbose_name='Содержимое', help_text='Введите текст')
    preview = models.ImageField(upload_to='articles/photo', blank=True, null=True, verbose_name='Изображение',
                              help_text='Загрузите изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания',
                                      help_text='Укажите дату создания')
    published = models.BooleanField(verbose_name='Опубликовано', help_text='Укажите статус', default=True)
    views_counter = models.PositiveIntegerField(verbose_name='Количество просмотров',
                                                help_text='Укажите количество просмотров', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title']

    def __str__(self):
        return self.title
