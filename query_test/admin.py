from django.contrib import admin
from .models import Worker, Bonus, Title, TableOne, TableTwo
# Register your models here.





@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display  = ['first_name', 'salary', 'department']


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    list_display  = ['worker', 'bonus_amount']


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display  = ['worker', 'worker_title']


@admin.register(TableOne)
class TableOneAdmin(admin.ModelAdmin):
    list_display  = ['data']

@admin.register(TableTwo)
class TableTwoAdmin(admin.ModelAdmin):
    list_display  = ['table_one_data']

