from tabnanny import verbose
from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Room or Experience Category"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = (
            "rooms",
            "Rooms",
        )
        EXPERIENCES = (
            "experiences",
            "Experiences",
        )

    name = models.CharField(
        max_length=100,
    )
    kind = models.CharField(
        max_length=50,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()} : {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
