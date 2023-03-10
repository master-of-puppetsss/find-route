from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название города'
    )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']

    def __str__(self) -> str:
        return f'{self.name}'
