# Generated by Django 3.2.7 on 2021-10-05 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_title_task_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='title2',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task',
            new_name='street',
        ),
    ]