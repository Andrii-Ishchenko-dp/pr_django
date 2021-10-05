from .models import Task
from django.forms import ModelForm, TextInput, Select
from  django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["country",'city',"street","name_task","surname","phone_num","account_pic"]
        widgets = {
            "country": TextInput(attrs={
                "class":"form-control",
                "placeholder":"Введите страну"
            }),
            "order": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите таблицы"
            }),
            "name_task": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите имя"
            }),
            "city": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите город"
            }),
            "task": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите улицу, номер дома..."
            }),
            "phone_num": TextInput(attrs={
                "class": "form-control",
                "placeholder": "+38"}),
            "surname": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Введите фамилию"}),


        }



# "str_char": Select(attrs={
#                 "class": "form-control"
#             }, choices= (['Выбор 1', 'Выбор 1'], ['Выбор 2', 'Выбор 2']))

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']