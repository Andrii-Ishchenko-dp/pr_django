import django_filters
from .models import *

class NameFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['name_task','surname','phone_num','title','title2','task']
