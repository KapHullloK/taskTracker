from django.core.management.base import BaseCommand
from users.models import User
from django.contrib.auth.hashers import make_password
import random

POSITIONS = [
    'Менеджер',
    'Разработчик',
    'Тестировщик',
    'Аналитик',
    'Дизайнер',
    'Администратор',
    'Специалист поддержки'
]

ACCESS_LEVELS = [20, 30, 30, 60, 70]


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        count = 10

        for i in range(count):
            username = f"test_user_{i}"
            full_name = f"test_user_{i}"
            email = ""
            position = random.choice(POSITIONS)
            access_level = random.choice(ACCESS_LEVELS)
            password = make_password('password')

            User.objects.create(
                username=username,
                full_name=full_name,
                email=email,
                position=position,
                access_level=access_level,
                password=password
            )

        self.stdout.write(self.style.SUCCESS(f'✅ Успешно создано {count} тестовых пользователей'))
