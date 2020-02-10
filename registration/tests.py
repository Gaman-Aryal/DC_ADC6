from django.test import TestCase, client
from registration.models import Buyer, Owner
from django.contrib.auth import authenticate
# Create your tests here.

class BuyerSigninTest(TestCase):

    def setUp(self):
        self.user = Buyer.objects.create(Username='gamanaryal', Password='gamanaryal12345', E_mail='gamanaryal12345@gmail.com')
        self.user.save()
    
    def test_correct(self):
        user = authenticate(username='gamanaryal', password='gamanaryal12345')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='gaman', password='gamanaryal12345')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='gamanaryal', password='gamanaryal12345')
        self.assertFalse(user is not None and user.is_authenticated)

class OwnerSigninTest(TestCase):

    def setUp(self):
        self.user = Owner.objects.create(Username='Prawjal', Password='Prawjal12345', E_mail='Prawjal1234512345@gmail.com')
        self.user.save()
    
    def test_correct(self):
        user = authenticate(username='Prawjal', password='Prawjal12345')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='Prawjal123', password='Prawjal12345')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='Prawjal', password='Prawjal12345')
        self.assertFalse(user is not None and user.is_authenticated)


