"""Админка для модели Task."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Админка для модели Task."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
