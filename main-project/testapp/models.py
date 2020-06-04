from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Rubric(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
        blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return reverse('testapp:rubric', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=255)
    category = TreeForeignKey(Rubric, on_delete=models.PROTECT)

    def __str__(self):
        return self.name