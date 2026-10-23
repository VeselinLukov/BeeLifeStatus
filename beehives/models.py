from django.db import models

from apiaries.models import Apiary


class Beehive(models.Model):
    class ColonyStatus(models.TextChoices):
        STRONG_COLONY = 'SC', 'Strong colony'
        MEDIUM_COLONY = 'MC', 'Medium colony'
        WEAK_COLONY = 'WC', 'Weak colony'
        SWARM = 'SW', 'Swarm'

    class BeehiveTypeChoice(models.TextChoices):
        DADANT_BLATT = 'DB', 'Dadant-Blatt'
        LANGSTROTH_RUTH = 'LR', 'Langstroth-Ruth'
        FARRAR = 'FR', 'Farrar'
        LONG_DEEP_HIVE = 'LD', 'Long deep hive'
        ROGER_DELON = 'RD', 'Roger-Delon'
        EPS = 'PS', 'Expanded polystyrene'

    beehive_number = models.PositiveIntegerField()
    beehive_type = models.CharField(
        max_length=2,
        choices=BeehiveTypeChoice.choices
    )
    installation_date = models.DateTimeField(
        auto_now_add=True
    )
    current_status = models.CharField(
        max_length=2,
        choices=ColonyStatus.choices
    )
    beehive_description = models.TextField()
    apiary = models.ForeignKey(
        to=Apiary,
        on_delete=models.CASCADE,
        related_name="beehives"
    )
