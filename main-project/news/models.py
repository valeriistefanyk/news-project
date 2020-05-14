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

    def __str__(self):
        return f"{self.id}. {self.title}"
