# Generated by Django 3.2.7 on 2021-10-05 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_task_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='full_name',
        ),
    ]