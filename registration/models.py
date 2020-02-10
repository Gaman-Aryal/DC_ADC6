from django.db import models
from django import forms


class Buyer(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    Username = models.CharField(max_length=10)
    Gender = models.CharField(max_length=25, default="Others")
    Phone_number = models.CharField(max_length=10)
    E_mail = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.First_Name} {self.Last_Name} is the name of the buyer"


class Owner(models.Model):
    First_Name = models.CharField(max_length=40)
    Last_Name = models.CharField(max_length=40)
    Username = models.CharField(max_length=10)
    Gender = models.CharField(max_length=25, default="Others")
    Phone_number = models.CharField(max_length=10)
    E_mail = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name} is the name of the owner"

