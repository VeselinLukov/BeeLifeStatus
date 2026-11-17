from django.db import models

from beehives.models import Beehive
from inspections.models import Inspection


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        IN_PROCESS = 'IP', 'In process'
        DONE = 'DN', 'Done'

    task_title = models.CharField(
        max_length=100,
        unique=True,
    )
    task_description = models.TextField()
    deadline = models.DateTimeField(

    )
    task_status = models.CharField(
        max_length=2,
        choices=TaskStatus.choices
    )
    inspection = models.ManyToManyField(
        to=Inspection,
        verbose_name="Inspections list"
    )

