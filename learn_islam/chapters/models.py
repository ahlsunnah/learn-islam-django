from django.db import models
from django.utils.translation import ugettext_lazy as _
from learn_islam.core import models as core_models
from learn_islam.courses.models import Course


class Chapter(models.Model):
    course = models.ForeignKey(
        Course,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    audio = models.URLField(_("Audio"), blank=True, max_length=255)
    duration = models.PositiveIntegerField(_("Duration"), blank=True)
    order = models.PositiveIntegerField(_("Order"), blank=True)
    slug = models.CharField(_("Slug"), blank=True, max_length=255)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.slug


class ChapterTranslation(models.Model):
    chapter = models.ForeignKey(
        Chapter, related_name='translations', on_delete=models.CASCADE
    )
    locale = core_models.LocaleField()
    title = models.CharField(_("Title"), max_length=200)
    transcription = models.TextField(_("Transcription"), blank=True)
    video = models.CharField(_("Video"), max_length=200)
    vocabulary = models.TextField(_("Vocabulary"), blank=True)

    class Meta:
        unique_together = (('locale', 'chapter'),)

    def __str__(self):
        return self.title
