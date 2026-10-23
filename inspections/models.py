from django.db import models

from beehives.models import Beehive


class Inspection(models.Model):
    class HealthStatus(models.TextChoices):
        HEALTHY = 'H', 'Healthy'
        SWARMING_RISK = 'SR', 'Swarming risk'
        BEING_ROBBED = 'BR', 'Being robbed'
        DISEASE_DETECTED = 'DD', 'Disease detected',
        LAYING_WORKERS = 'LW', 'Laying workers'

    class QueenStatus(models.TextChoices):
        QUEENRIGHT = 'QR', 'Queenright'
        QUEENLESS = 'QL', 'Queenless'
        REQUEENED = 'RQ', 'Requeened'
        QUEEN_CELLS = 'QC', 'Queen cells'

    inspection_date = models.DateTimeField(
        auto_now_add=True
    )
    colony_health = models.CharField(
        max_length=2,
        choices=HealthStatus.choices
    )
    queen_status = models.CharField(
        max_length=2,
        choices=QueenStatus.choices
    )
    food_stores = models.TextField()
    inspection_notes = models.TextField(
        blank=True,
        null=True
    )
    beehive = models.ForeignKey(
        to=Beehive,
        on_delete=models.CASCADE,
        related_name="inspections"
    )

