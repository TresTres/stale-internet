from django.contrib import admin

from db_admin.themes.models import Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "timestamp")
