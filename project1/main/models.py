from django.db import models
import uuid

class Task(models.Model):
    # owner=
    name_task = models.CharField('Название', max_length=50)
    title = models.CharField('Название', max_length= 50)
    title2 = models.CharField('Название', max_length=50)
    task = models.CharField('Описание', max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    column_sep = models.CharField('Разделитель', max_length= 50)
    int_min = models.IntegerField(default=0)
    int_max = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    str_char = models.CharField('Скобки', max_length=50)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Review(models.Model):
    project = models.ForeignKey(Task, on_delete=models.CASCADE, null= True, blank= True)
    body = models.TextField(null=True, blank=True)


