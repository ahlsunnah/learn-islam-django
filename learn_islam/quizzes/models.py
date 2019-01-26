from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from learn_islam.courses.models import Course


class Quiz(models.Model):
    course = models.ForeignKey(
        Course,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    difficulty = models.PositiveIntegerField(_("Difficulty"), blank=True)
    type = models.CharField(_("Slug"), blank=True, max_length=20)

    # def __str__(self):
    #     return self.slug


class QuizTranslation(models.Model):
    quiz = models.ForeignKey(
        Quiz, related_name='translations', on_delete=models.CASCADE
    )
    data = JSONField()
    locale = models.CharField(max_length=10)

    class Meta:
        unique_together = (('locale', 'quiz'),)

    # def __str__(self):
    #     return self.title
