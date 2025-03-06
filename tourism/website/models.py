from django.db import models
import datetime
# Create your models here.
class Users(models.Model):
    email=models.CharField(max_length=50,unique=True,null=False)
    name=models.CharField(max_length=100,unique=False,null=False)
    password=models.CharField(max_length=64,null=False)
    nickname=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=50,default="Nepal")
    gender=models.CharField(max_length=6,null=True)
    profile=models.CharField(max_length=100,default="default.png")
    date=models.DateField(default=datetime.date.today)
    def __str__(self):
        return f"{self.name} as {self.email}"

class Destinations(models.Model):
    name=models.CharField(max_length=30,null=False)
    imagename=models.CharField(max_length=50,unique=False,null=False)
    times=models.CharField(max_length=20,unique=False,null=False)
    price=models.IntegerField(null=False)
    description=models.CharField(max_length=100,unique=False,null=True)
    def __str__(self):
        return f"{self.name} at {self.imagename}"