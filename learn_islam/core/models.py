from django.db import models
from django.utils.translation import ugettext_lazy as _

LANGUAGES_CHOICES = [
    ('ar', 'العربية'),
    ('fr', 'Français')
]

class LocaleField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = _("Language")
        kwargs['choices'] = LANGUAGES_CHOICES
        kwargs['max_length'] = 10
        super().__init__(*args, **kwargs)
