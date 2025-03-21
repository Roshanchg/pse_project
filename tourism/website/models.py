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
    price_in_k=models.IntegerField(null=False,default=0)
    time=models.CharField(max_length=100,null=False,default="3 Days, 3 Nights")
    ptype=models.CharField(max_length=100,null=True)
    bookingcount=models.IntegerField(null=False,default=0)
    def __str__(self):
        return f"{self.destination} for {self.price_in_k}K for {self.time}"

class Payment_Info(models.Model):
    number=models.CharField(max_length=100,null=False,default='0000000')
    exp=models.CharField(max_length=10,null=False,default="00/00")
    cvc=models.CharField(max_length=50,null=False,default="00000")
    holder=models.CharField(max_length=100,null=False)
    country=models.CharField(max_length=100,null=False)
    city=models.CharField(max_length=100,null=False)
    state=models.CharField(max_length=100,null=False)
    def __str__(self):
        return f"{self.holder}'s card, number {self.number}"


class Bookings(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE)
    package=models.ForeignKey(Packages,on_delete=models.CASCADE)
    dateToBook=models.DateField(default=datetime.date.today)
    bookedWhen=models.DateField(default=datetime.date.today)
    payment=models.ForeignKey(Payment_Info,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total=models.IntegerField(default=-1)
    def __str__(self):
        return f"{self.package} by {self.user} at {self.bookedWhen} for {self.dateToBook} total: {self.total}"
