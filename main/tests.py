from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

class TaskTestCases(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username = "testuser", password="123zxcVBN")
        self.accaunt = Task.objects.create(
            name_task = 'Test',
            surname = 'User',
            phone_num = '123456',
            title = 'Test_count',
            title2 = 'test_city',
            task = 'test_street'
        )
