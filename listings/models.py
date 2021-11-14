import uuid
import math

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from .choices import County, PropertyType


class Listing(TimeStampedModel, models.Model):
    class Meta:
        ordering = ["-created"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = AutoSlugField(populate_from=["title", "id"])
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    county = models.CharField(max_length=50, choices=County.get_choices())
    area = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms  = models.PositiveIntegerField()
    car_spaces = models.PositiveIntegerField()
    property_type = models.CharField(max_length=50, choices=PropertyType.get_choices())
    year = models.PositiveSmallIntegerField()
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listing-detail", kwargs={"slug": self.slug})

    def get_price_euros(self):
        return math.ceil(self.price / (100.0 * 7.51)) * 100

    def get_readable_county(self):
        return self.county.replace("_", "-")
