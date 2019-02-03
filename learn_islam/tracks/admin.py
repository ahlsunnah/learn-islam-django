from django.contrib import admin

from .models import Track, TrackTranslation


class TrackTranslationInline(admin.TabularInline):
    model = TrackTranslation
    fields = ('locale', 'title', 'description')
    ordering = ('locale',)
    min_num = 2
    extra = 0


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('slug', 'order', 'soon')
    list_filter = ('soon', )
    inlines = [
        TrackTranslationInline,
    ]
