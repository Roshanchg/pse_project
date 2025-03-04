from django.db import models

# Create your models here.
class Users(models.Model):
    email=models.CharField(max_length=50,unique=True,null=False)
    name=models.CharField(max_length=100,unique=False,null=False)
    password=models.CharField(max_length=64,null=False)
    def __str__(self):
        return f"{self.name} as {self.email}"

    