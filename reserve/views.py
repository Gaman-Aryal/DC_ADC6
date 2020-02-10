from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse
from rooms.models import Room
from .models import Reserve, Book
from django.contrib import messages
import reserve


def get_user_pending_order(request):
    user_profile = get_object_or_404(User, username=request.user)
    order = Reserve.objects.filter(user=user_profile)
    if order.exists():
        return order[0]
    return 0

def add_to_cart(request, id):
    user_profile = get_object_or_404(User, username=request.user)
    rooms = Room.objects.get(id=id)
    order_item, status = Book.objects.get_or_create(room=rooms)
    user_order, status = Reserve.objects.get_or_create(user=user_profile)
    # total_price = rooms.Room_price
    # # total_price = total_price + Room.Room_price ,{'total_price'= total_price}
    user_order.rooms.add(order_item)

    if status:
        user_order.save()

    return redirect(reverse('carts'))

def delete_from_cart(request, id):
    item_to_delete = Book.objects.filter(pk=id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
    return redirect(reverse('carts'))


def cart_details(request):
    show_order = get_user_pending_order(request)
    context = {
        'order': show_order
    }
    return render(request, 'cart.html', context)


