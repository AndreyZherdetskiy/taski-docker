from django.db import models


class Task(models.Model):
    """Модель задачи для трекера задач.

    Атрибуты:
        title (str): Заголовок задачи.
        description (str): Описание задачи.
        completed (bool):
            Статус выполнения задачи.
    """
    title: models.CharField = models.CharField(
        verbose_name='Заголовок',
        max_length=120
    )
    description: models.TextField = models.TextField()
    completed: models.BooleanField = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Строковое представление задачи."""
        return self.title
