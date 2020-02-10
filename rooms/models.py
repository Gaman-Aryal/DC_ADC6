from django.contrib.auth.models import User
from django.db import models
from decimal import *


class Room(models.Model):
    Room_owner = models.CharField(max_length=60)
    Room_phnumber = models.IntegerField()
    Room_location = models.CharField(max_length=200)
    Room_price = models.DecimalField(decimal_places=2, max_digits=7, default=4000.00)
    pub_date = models.DateField(default=2019/12/12)
    Room_desc = models.CharField(max_length=500)
    file = models.ImageField(upload_to='media')

    def __str__(self):
        return self.Room_desc
        
    def test_room_owner(self):
        return self.Room_owner

    def count_rooms(self):
        return self.rooms.all().count()

    def uploadata_fields_blank(self):
        return(self.Room_desc!= False)

    def TestRoom_desc(self):
        return (len(self.Room_desc) >= 3) and (len(self.Room_desc) <= 400) 
 
    def TestRoom_Price(self):
        return ((self.Room_price) >= 3500.00) and ((self.Room_price) <= 12000.00)

    def TestOwnerNameAndOwnerDesc(self):
        return (self.Room_owner != self.Room_desc)