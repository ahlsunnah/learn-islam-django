from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from learn_islam.progress.models import Progress

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    pass
