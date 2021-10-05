from django.db import models


class Task(models.Model):
    name_task = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50, default='')
    phone_num = models.CharField('Номер телефона', max_length=50, default='')
    title = models.CharField('Страна', max_length= 50)
    title2 = models.CharField('Город', max_length=50)
    task = models.CharField('Улица', max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    account_pic = models.ImageField(null=True, blank=True)


    def __str__(self):
        return  self.name_task

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        unique_together = 'name_task', 'surname'


# class Review(models.Model):
#     project = models.ForeignKey(Task, on_delete=models.CASCADE, null= True, blank= True)
#     body = models.TextField(null=True, blank=True)


