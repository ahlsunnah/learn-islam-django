from django.db import models
from django.utils.translation import ugettext_lazy as _


class Topic(models.Model):
    color = models.CharField(_("Color"), blank=True, max_length=20)
    level = models.PositiveIntegerField(_("Level"), blank=True)
    order = models.PositiveIntegerField(_("Order"), blank=True)
    slug = models.CharField(_("Slug"), blank=True, max_length=255)

    def __str__(self):
        return self.slug


class TopicTranslation(models.Model):
    topic = models.ForeignKey(
        Topic, related_name='translations', on_delete=models.CASCADE
    )
    locale = models.CharField(max_length=10)
    title = models.CharField(_("Title"), max_length=20)

    class Meta:
        unique_together = (('locale', 'topic'),)

    def __str__(self):
        return self.title
