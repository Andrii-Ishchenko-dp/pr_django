from .models import Task
from django.forms import ModelForm, TextInput
from  django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title",'title2',"task","name_task","column_sep","str_char"]
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
                "placeholder": "Введите таблицы"
            }),
            "title2": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название"
            }),
            "task": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название"
            }),
            "str_char": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите название"
            }),
            "column_sep": TextInput(attrs={
                "class": "form-control"})
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']