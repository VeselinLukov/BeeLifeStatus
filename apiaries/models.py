from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Apiary(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            RegexValidator(
                regex=r'[A-Za-z0-9]+',
                message="Ensure the name contains only letters and numbers!"
            )
        ]
    )
    location = models.CharField(
        max_length=100
    )
    number_of_hives = models.PositiveIntegerField(
        default=0
    )
    apiary_description = models.TextField(
        blank=True,
        null=True
    )
    image_url = models.URLField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
