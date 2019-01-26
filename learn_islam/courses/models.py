from django.db import models
from django.utils.translation import ugettext_lazy as _

from learn_islam.topics.models import Topic
from learn_islam.tracks.models import Track


class Course(models.Model):
    topic = models.ForeignKey(
        Topic,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    track = models.ForeignKey(
        Track,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    level = models.PositiveIntegerField(_("Level"), blank=True)
    order = models.PositiveIntegerField(_("Order"), blank=True)
    slug = models.CharField(_("Slug"), blank=True, max_length=255)

    def __str__(self):
        return self.slug


class CourseTranslation(models.Model):
    course = models.ForeignKey(
        Course, related_name='translations', on_delete=models.CASCADE
    )
    description = models.CharField(_("Description"), blank=True, max_length=500)
    locale = models.CharField(max_length=10)
    title = models.CharField(_("Title"), max_length=200)

    class Meta:
        unique_together = (('locale', 'course'),)

    def __str__(self):
        return self.title
