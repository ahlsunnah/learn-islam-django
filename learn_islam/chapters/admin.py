from django.contrib import admin

from .models import Chapter, ChapterTranslation


class ChapterTranslationInline(admin.StackedInline):
    model = ChapterTranslation
    fields = ('locale', 'title', 'video', 'transcription', 'vocabulary')
    ordering = ('locale',)
    min_num = 2
    extra = 0


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('slug', 'order', 'course')
    list_filter = ('course', )
    ordering = ('course__order', 'order')
    fields = ('course', 'order', 'slug', 'audio', 'duration')
    inlines = [
        ChapterTranslationInline,
    ]
