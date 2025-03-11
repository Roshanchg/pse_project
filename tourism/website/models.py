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
    name=models.CharField(max_length=100,null=False)
    image=models.CharField(max_length=100,default="destinations/mustang.png")
    def __str__(self):
        return self.name

class Packages(models.Model):
    destination=models.ForeignKey(Destinations,on_delete=models.CASCADE)
    desc=models.CharField(max_length=500,null=False)
    price=models.IntegerField(null=False,default=0)
    time=models.CharField(max_length=100,null=False,default="3 Days, 3 Nights")
    ptype=models.CharField(max_length=100,null=True)
    bookingcount=models.IntegerField(null=False,default=0)
    def __str__(self):
        return f"{self.destination} for {self.price} for{self.time}"

class Bookings(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    package=models.ForeignKey(Packages,on_delete=models.CASCADE)
    dateToBook=models.DateField(default=datetime.date.today)
    bookedWhen=models.DateField(default=datetime.date.today)
    def __str__(self):
        return f"{self.package} by {self.user} at {self.bookedWhen} for {self.dateToBook}"