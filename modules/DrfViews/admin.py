from django.contrib import admin
from .models.basic_models import Department, Empolyee, Company
# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display  = ['company', 'name']


@admin.register(Empolyee)
class EmpolyeeAdmin(admin.ModelAdmin):
    list_display  = ['department', 'name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display  = ['name']

