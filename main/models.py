from django.db import models
import uuid


class Task(models.Model):
    name_task = models.CharField('Имя', max_length=50)
    title = models.CharField('Страна', max_length= 50)
    title2 = models.CharField('Город', max_length=50)
    task = models.CharField('Улица', max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    surname = models.CharField('Фамилия', max_length= 50, default='')
    phone_num = models.CharField('Номер телефона', max_length=50, default='')
    #id=models.CharField(primary_key=True,default=uuid.uuid4, editable=False, max_length=36)

    def __str__(self):
        return  self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Review(models.Model):
    project = models.ForeignKey(Task, on_delete=models.CASCADE, null= True, blank= True)
    body = models.TextField(null=True, blank=True)


