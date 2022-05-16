from django.db import models
from django.db.models import Q
import uuid

class CommonFieldMixinModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
       abstract = True



class Worker(CommonFieldMixinModel):
    worker_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name =  models.CharField(max_length=25)
    last_name =  models.CharField(max_length=25)
    salary = models.IntegerField()
    joining_date = models.DateTimeField()
    department =  models.CharField(max_length=25)

    def __str__(self):
        return f"{self.first_name}"



class Bonus(CommonFieldMixinModel):
    worker = models.ForeignKey(Worker, 
                    related_name='bonus', 
                    on_delete=models.CASCADE, 
                    blank=False, 
                    null=False)
    bonus_date = models.DateTimeField()
    bonus_amount = models.IntegerField()

    def __str__(self):
        return f"{self.worker.first_name}"


class Title(CommonFieldMixinModel):
    worker = models.ForeignKey(Worker, 
                    related_name='title', 
                    on_delete=models.CASCADE, 
                    blank=False, 
                    null=False)
    worker_title = models.CharField(max_length=25)
    affected_from = models.DateTimeField()
    
    def __str__(self):
        return f"{self.worker.first_name}"





# transaction model test

class TableOne(CommonFieldMixinModel):
    data = models.CharField(max_length=10)

    class Meta:
        db_table = 'tbl_one'
        app_label = 'query_test'
        get_latest_by = "updated_at"
        #constraints = [
        #    models.CheckConstraint(check = Q(data='Mindblow'), name='check_data'),]
        # date base level contrains
        # https://www.w3schools.com/sql/sql_constraints.asp
        # https://docs.djangoproject.com/en/4.0/ref/models/constraints/#module-django.db.models.constraints
        

class TableTwo(CommonFieldMixinModel):
    table_one_data =  models.ForeignKey(TableOne, on_delete= models.CASCADE)
    class Meta:
        order_with_respect_to = 'table_one_data'
