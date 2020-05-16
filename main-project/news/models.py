from django.db import models


class News(models.Model):
    """ Модель новостей """

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
        ordering = ['-created_at']

    title = models.CharField(max_length=200, verbose_name='Назва')
    content = models.TextField(verbose_name='Текст новини')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Відредаговано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категорія')

    def __str__(self):
        return f"{self.id}. {self.title}"


class Category(models.Model):
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']

    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')
    description = models.TextField(blank=True, null=True, verbose_name='Опис категорії')

    def __str__(self):
        return f"{self.id}. {self.title}"