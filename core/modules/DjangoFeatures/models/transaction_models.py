from django.db import models
from django.db.models import Q
import uuid

class CommonFieldMixinModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
       abstract = True



# transaction model test

class TableOne(CommonFieldMixinModel):
    data = models.CharField(max_length=12)

class TableTwo(CommonFieldMixinModel):
    table_one_data =  models.ForeignKey(TableOne, on_delete= models.CASCADE)
    data = models.CharField(max_length=12, blank=False, null=False)
    
