from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experience Model Definition"""

    name = models.CharField(
        max_length=250,
    )
    country = models.CharField(
        max_length=100,
        default="한국",
    )
    city = models.CharField(
        max_length=100,
        default="서울",
    )
    description = models.TextField()
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=250,
    )
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(
        max_length=250,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        null=True,
    )
    explanation = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
