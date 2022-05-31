from django.contrib import admin
from .models.model_uploads import UploadTbl

@admin.register(UploadTbl)
class ForestAdmin(admin.ModelAdmin):
    list_display  = ['file', 'photo', 'id_prof']

