from datetime import timezone
from django.db import models
from django.template.backends import django
from django.utils import timezone
from django.urls import reverse


class ToDo(models.Model):
    title = models.CharField('Название задания', max_length=500)
    description = models.TextField('Описание задания', max_length=500)
    completed = models.BooleanField('Завершено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title

