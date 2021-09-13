# Generated by Django 3.2.7 on 2021-09-09 20:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210908_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='title2',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
