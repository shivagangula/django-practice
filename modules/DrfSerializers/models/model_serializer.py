from django.db import models


class Forest(models.Model):
    name =  models.CharField(max_length=25)
    tree_count = models.IntegerField()
    location = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"


        