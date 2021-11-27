from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField

from ckeditor.fields import RichTextField

from .choices import Category

class BlogPost(TimeStampedModel, models.Model):
    title = models.CharField(max_length=200)
    lead = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    slug = AutoSlugField(populate_from=["title"])
    category = models.CharField(max_length=50, choices=Category.get_choices())
    body = RichTextField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"slug": self.slug})