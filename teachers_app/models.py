import uuid
from django.db import models

# Create your models here.

class student_profile(models.Model):
    name=models.CharField(max_length=50)
    student_id=models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email=models.EmailField(max_length=254)
    courses=models.TextField(blank=True)
    phone=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class courses_detail(models.Model):
    title=models.CharField(max_length=256)
    code=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    department=models.CharField(max_length=500)
    teacher=models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
class department_mod(models.Model):
    department=models.CharField(max_length=256)
    
    def __str__(self):
        return self.department
    
    