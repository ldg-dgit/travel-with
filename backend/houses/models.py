from email.policy import default
from django.db import models


class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=200)
    pets_allowed = models.BooleanField(
        default=False,
        help_text="Does this house allows pets?",
        verbose_name="Pets allowed?",
    )

    def __str__(self):
        return self.name
