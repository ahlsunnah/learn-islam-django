from django.db import models
from django.utils.translation import ugettext_lazy as _
from learn_islam.core import models as core_models
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

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.slug

    @property
    def quiz_difficulties(self):
        one_quiz_by_difficulty = self.quiz_set.order_by('difficulty').distinct('difficulty')
        return list(map(lambda quiz: quiz.difficulty, one_quiz_by_difficulty))


class CourseTranslation(models.Model):
    course = models.ForeignKey(
        Course, related_name='translations', on_delete=models.CASCADE
    )
    description = models.CharField(_("Description"), blank=True, max_length=500)
    locale = core_models.LocaleField()
    title = models.CharField(_("Title"), max_length=200)

    class Meta:
        unique_together = (('locale', 'course'),)

    def __str__(self):
        return self.title
