from django.contrib import admin
from .models.oo_models import Bottle, Cap




@admin.register(Bottle)
class BottleAdmin(admin.ModelAdmin):
    list_display  = ['bottle_name']



@admin.register(Cap)
class CapAdmin(admin.ModelAdmin):
    list_display  = ['bottle']