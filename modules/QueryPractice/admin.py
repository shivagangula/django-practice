from django.contrib import admin
from modules.QueryPractice.models.basic_models import Worker, Bonus, Title
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

