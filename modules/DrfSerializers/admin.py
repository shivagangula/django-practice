from django.contrib import admin
from .models.model_serializer import Forest


@admin.register(Forest)
class ForestAdmin(admin.ModelAdmin):
    list_display  = ['name', 'tree_count', 'location']

