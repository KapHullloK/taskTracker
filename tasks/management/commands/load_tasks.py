from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from tasks.models import Task
from users.models import User
import random


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user_count = User.objects.count()
        if user_count == 0:
            self.stdout.write(self.style.ERROR('Нет пользователей в БД. Сначала создайте пользователей.'))
            return

        users = list(User.objects.all())

        statuses = ['created', 'in_process', 'finalized']
        task_titles = [
            'Подготовить отчет',
            'Провести встречу с командой',
            'Обновить документацию',
            'Отправить рассылку',
            'Проверить баги',
            'Разработать фичу',
            'Тестирование производительности',
        ]

        tasks = []

        for i in range(10):
            title = f"{random.choice(task_titles)} #{i + 1}"
            description = f"Подробное описание задачи {title}. Необходимо выполнить до дедлайна."
            performer = random.choice(users)
            deadline = timezone.now().date() + timedelta(days=random.randint(1, 30))
            status = random.choice(statuses)

            tasks.append(Task(
                title=title,
                description=description,
                performer=performer,
                deadline=deadline,
                status=status
            ))

        Task.objects.bulk_create(tasks)

        self.stdout.write(self.style.SUCCESS('✅ Тестовые задачи успешно загружены в БД'))
