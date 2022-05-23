from django.db import models

class Bottle(models.Model):
    bottle_name = models.CharField(max_length=10)


class Cap(models.Model):
    bottle =  models.OneToOneField(
         Bottle, 
         on_delete = models.CASCADE)



