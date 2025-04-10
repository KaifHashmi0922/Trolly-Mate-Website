from django.db import models
from datetime import date

# Create your models here.
from django.db import models

# Create your models here.
class Customer(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    father=models.CharField(max_length=100)
    email=models.EmailField()
    pass1=models.CharField(max_length=100)
    Phone=models.CharField(unique=True,max_length=10)
    image=models.FileField(upload_to="uploads/users/",null=True)
    address=models.CharField(max_length=255,null=True)
    
    
class Shoping(models.Model):
    p_id=models.CharField(max_length=20,null=True)
    p_name=models.CharField(max_length=100)
    p_quantity=models.IntegerField(null=True)
    p_price=models.IntegerField()
    p_image=models.FileField(upload_to="uploads/Shoping/",null=True)
    p_date=models.CharField(max_length=100) 
    status=models.BooleanField(null=True)
    
    
    
