from django.db import models
import uuid

class BaseField(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
       abstract = True


class Department(BaseField):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name  = models.CharField(max_length=25, blank=False, null=False)
    
    @classmethod
    def get_departments_count(cls):
        return cls.objects.all().count()

    def __str__(self):
        return f"{self.name} : {self.uuid}"



class Empolyee(BaseField):
    department = models.ForeignKey(
                    Department,
                    related_name='employees', 
                    on_delete=models.CASCADE, 
                    blank=False, 
                    null=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name  = models.CharField(max_length=25, blank=False, null=False)
    
    
    @classmethod
    def get_empolyee_count(cls):
        return cls.objects.all().count()

    def __str__(self):
        return f"{self.name} : {self.uuid}"


