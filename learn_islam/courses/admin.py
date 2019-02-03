from django.contrib import admin

from .models import Course, CourseTranslation


class CourseTranslationInline(admin.TabularInline):
    model = CourseTranslation
    fields = ('locale', 'title', 'description')
    ordering = ('locale',)
    min_num = 2
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('slug', 'order', 'track', 'topic')
    list_filter = ('track', 'topic')
    ordering = ('track__order', 'order')
    fields = ('track', 'topic', 'order', 'slug')
    inlines = [
        CourseTranslationInline,
    ]
