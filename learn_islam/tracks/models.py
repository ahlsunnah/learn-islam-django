from django.db import models
from django.utils.translation import ugettext_lazy as _


class Track(models.Model):

    order = models.PositiveIntegerField(_("Order"), blank=True)
    level = models.PositiveIntegerField(_("Level"), blank=True)
    slug = models.CharField(_("Slug"), blank=True, max_length=255)
    soon = models.BooleanField(_("Coming Soon"), default=False, blank=True)
