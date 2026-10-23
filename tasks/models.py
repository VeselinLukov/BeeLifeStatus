from django.db import models

from beehives.models import Beehive
from tags.models import Tag


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        IN_PROCESS = 'IP', 'In process'
        DONE = 'DN', 'Done'

    task_title = models.CharField(
        max_length=100
    )
    task_description = models.TextField()
    deadline = models.DateTimeField()
    task_status = models.CharField(
        max_length=2,
        choices=TaskStatus.choices
    )
    beehives = models.ManyToManyField(
        to=Beehive,
        verbose_name="Beehives list"
    )
    tags = models.ManyToManyField(
        to=Tag,
        verbose_name="Tags list"
    )

