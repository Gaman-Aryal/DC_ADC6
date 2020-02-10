from django.test import TestCase, Client
from rooms.models import Room
from reserve.models import Book

# Create your tests here.

class ModelTestCase(TestCase):
    def test_count_rooms(self):
        a1 = Room.objects.create(Room_owner="Gaman", Room_location="Kathamndu",Room_phnumber=9848765833, Room_price=8000.00, pub_date="2015-02-02", 
        Room_desc="This is  room" )
        value = a1.count_rooms()
        self.assertNotEqual(value,1)

    def test_Room_desc(self):
        a1 = Room.objects.create(Room_owner="Gaman", Room_location="Kathamndu",Room_phnumber=9848765833, Room_price=8000.00, pub_date="2015-02-02", 
        Room_desc="This is  room" )
        value = a1.TestRoom_desc()
        self.assertTrue(value)

    def test_Room_Price(self):
        a1 = Room.objects.create(Room_owner="Gaman", Room_location="Kathamndu",Room_phnumber=9848765833, Room_price=8000.00, pub_date="2015-02-02", 
        Room_desc="This is  room" )
        value = a1.TestRoom_Price()
        self.assertTrue(value)

    def test_OwnerNameAndOwnerDesc(self):
        name_desc_validation=Room.objects.create(Room_owner="Gaman",Room_desc="kathmandu", 
        Room_phnumber=9848765833, Room_price=8000.00, pub_date="2015-02-02")
        self.assertTrue(name_desc_validation.TestOwnerNameAndOwnerDesc())

    def test_Room_owner(self):
        owner_validation=Room.objects.create(Room_desc="kathmandu", 
        Room_phnumber=9848765833, Room_price=8000.00, pub_date="2015-02-02")
        self.assertFalse(owner_validation.test_room_owner())