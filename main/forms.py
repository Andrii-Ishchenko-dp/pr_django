from .models import Task
from django.forms import ModelForm, TextInput, Select
from  django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title",'title2',"task","name_task","column_sep"]
        widgets = {
            "title": TextInput(attrs={
                "class":"form-control",
                "placeholder":"Введите название"
            }),
            "int_min": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите таблицы"
            }),
            "int_max": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите таблицы"
            }),
            "order": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите таблицы"
            }),
            "name_task": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите имя"
            }),
            "title2": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название"
            }),
            "task": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название"
            }),
            "str_char": Select(attrs={
                "class": "form-control"
            }, choices= (['фигурные', '{}'], ['квадратные', '[]'])),
            "column_sep": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите фамилию"})
        }


# "str_char": Select(attrs={
#                 "class": "form-control"
#             }, choices= (['фигурные', '{}'], ['квадратные', '[]']))

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']