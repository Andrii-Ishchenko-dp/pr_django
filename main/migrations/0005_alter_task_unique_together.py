# Generated by Django 3.2.7 on 2021-10-05 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_task_full_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('name_task', 'surname')},
        ),
    ]
