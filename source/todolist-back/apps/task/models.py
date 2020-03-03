from django.db import models
from django.utils import timezone


class TaskManager(models.Manager):

    def active(self):
        return (
            self.get_queryset()
            .filter(finished_at__isnull=True)
            .order_by("created_at")
        )


class Task(models.Model):
    content = models.CharField("タスク", max_length=100)
    created_at = models.DateTimeField("登録日時", default=timezone.localtime)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    finished_at = models.DateTimeField("完了日時", null=True)

    objects = TaskManager()
