from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=52)
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список товаров'
        verbose_name_plural = 'Товары'