from email.policy import default
from django.db import models
from common.models import CommonModel


class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(
        max_length=200,
    )
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"


class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = (
            "entire_place",
            "Entire Place",
        )
        PRIVATE_ROOM = (
            "private_room",
            "Private Room",
        )
        SHARED_ROOM = (
            "shared_room",
            "Shared Room",
        )

    name = models.CharField(
        max_length=200,
        default="",
    )
    country = models.CharField(
        max_length=100,
        default="한국",
    )
    city = models.CharField(
        max_length=100,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=500,
    )
    pet_friendly = models.BooleanField(
        default=False,
    )
    kind = models.CharField(
        max_length=200,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )

    def __str__(self) -> str:
        return self.name
