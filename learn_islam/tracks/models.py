from django.db import models
from django.utils.translation import ugettext_lazy as _


class Track(models.Model):
    order = models.PositiveIntegerField(_("Order"), blank=True)
    slug = models.CharField(_("Slug"), blank=True, max_length=255)
    soon = models.BooleanField(_("Coming Soon"), default=False, blank=True)


class TrackTranslation(models.Model):
    track = models.ForeignKey(
        Track, related_name='translations', on_delete=models.CASCADE
    )
    description = models.CharField(_("Description"), blank=True, max_length=500)
    locale = models.CharField(max_length=10)
    title = models.CharField(_("Title"), max_length=20)

    class Meta:
        unique_together = (('locale', 'track'),)

    def __str__(self):
        return self.title
