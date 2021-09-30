import django_filters
from .models import *
from django.forms import ModelForm, TextInput

class NameFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created_time','account_pic']
        widgets = {
            "name_task": TextInput(attrs={
                "class": "form-control",
                "method": "get"
            }),
            "surname": TextInput(attrs={
                "class": "form-control"
            }),
            "phone_num": TextInput(attrs={
                "class": "form-control"
            }),
            "title": TextInput(attrs={
                "class": "form-control"
            }),
            "title2": TextInput(attrs={
                "class": "form-control"
            }),
            "task": TextInput(attrs={
                "class": "form-control"
            }),
        }