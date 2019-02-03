from django.contrib import admin

from .models import Topic, TopicTranslation


class TopicTranslationInline(admin.TabularInline):
    model = TopicTranslation
    ordering = ('locale',)
    min_num = 2
    extra = 0


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    fields = ('order', 'slug', 'level', 'color')
    list_display = ('slug', 'order', 'color')
    inlines = [
        TopicTranslationInline,
    ]
