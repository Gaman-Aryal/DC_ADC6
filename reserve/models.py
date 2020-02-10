from django.contrib.auth.models import User
from django.db import models
from registration.models import Owner, Buyer
from rooms.models import Room


class Book(models.Model):
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name="rooms")
    number = models.IntegerField(default=1)

    def __str__(self):
        return self.room.Room_owner

    def room_price(self):
        return self.number * self.room.Room_price


class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rooms = models.ManyToManyField(Book)

    def get_rooms(self):
        return self.rooms.all()

    def get_total(self):
        total = 0
        for order_item in self.rooms.all():
            total += order_item.room_price()
        return total

    def __str__(self):
        return '{0} - {1}'.format(self.user)

    def count_rooms(self):
        return self.rooms.all().count()