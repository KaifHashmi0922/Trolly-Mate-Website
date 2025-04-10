from django.db import models


# Create your models here.
class Admin(models.Model):
    uname=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    status=models.BooleanField()
    
    
    
class Categorys(models.Model):
    name=models.CharField(max_length=255)
    feature=models.CharField(max_length=255)
    status=models.BooleanField(null=True)
    def __str__(self):
        return self.name
    
class Companys(models.Model):
    name=models.CharField(max_length=255)
    types=models.ForeignKey(Categorys,on_delete=models.CASCADE,null=True)
    c_info=models.CharField(max_length=255,null=True)
    image=models.FileField(upload_to='uploads/companys/')
    status=models.BooleanField(null=True)
    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE,null=True)
    company=models.ForeignKey(Companys,on_delete=models.CASCADE,null=True)
    des=models.CharField(max_length=255)
    image=models.FileField(upload_to='uploads/products/') 
    Product_Quantity=models.IntegerField(null=True) 
    status=models.BooleanField(null=True)     