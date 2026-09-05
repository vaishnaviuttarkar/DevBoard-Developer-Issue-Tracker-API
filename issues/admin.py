from django.contrib import admin
from .models import Issue

# Register your models here.
# admin.site.register(Issue)

@admin.register(Issue)
class customIssue(admin.ModelAdmin):
    list_display = ("id", "title", "status", "priority", "assigned_to")