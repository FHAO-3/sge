from django.contrib import admin
from ai.models import AIResult


@admin.register(AIResult)
class AiResultAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'result',]
