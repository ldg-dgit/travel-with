from django.db import models


class House(models.Model):

    """Model Definition for Houses"""

    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=200)
