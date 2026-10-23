from django.db import models

from inspections.models import Inspection


class Tag(models.Model):
    tag_name = models.CharField(
        max_length=100
    )
    color = models.CharField(
        max_length=50
    )
    tag_description = models.TextField(
        blank=True
    )
    inspections = models.ManyToManyField(
        to=Inspection,
        verbose_name="Inspections list"
    )
