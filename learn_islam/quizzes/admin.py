from django.contrib import admin

from .models import Quiz, QuizTranslation
from .forms import QuizTranslationForm


class QuizTranslationInline(admin.TabularInline):
    model = QuizTranslation
    form = QuizTranslationForm
    fields = ('locale', 'data')
    ordering = ('locale',)
    min_num = 2
    extra = 0


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('course', 'difficulty', 'type')
    fields = ('course', 'difficulty', 'type')
    inlines = [
        QuizTranslationInline,
    ]
