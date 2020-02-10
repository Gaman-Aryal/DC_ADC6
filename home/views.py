from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse , reverse
from django.contrib.auth.decorators import permission_required
from registration.models import Buyer, Owner
from rooms.models import Room
from django.contrib.auth import logout
from django.db.models import Q
from reserve.models import Reserve , Book
from django.shortcuts import render, redirect, get_object_or_404


def homepage(request):
    if request.method == "GET":
        Room_list = Room.objects.all()[0:3]
        return render(request, 'index.html', {'Room_list': Room_list})

def logout_view(request):
    logout(request)
    return HttpResponse('<h2> You are logged out from the Rent it</h2><br><br><br><a href="/"><h1>Home Page</h1></a>')

def search(request):
    if request.method == "GET":
        src = request.GET['search']
        match = Room.objects.filter(Q(Room_location__startswith=src))
        match1 = Room.objects.filter(Q(Room_owner__startswith=src))
        match2 = Room.objects.filter(Q(Room_desc__startswith=src))
        match3 = Room.objects.filter(Q(id__startswith=src))

        if match:
            return render(request, 'index.html', {'source': match})
        elif match1:
            return render(request, 'index.html', {'source': match1})
        elif match2:
            return render(request, 'index.html', {'source': match2})
        elif match3:
            return render(request, 'index.html', {'source': match3})
        else:
            return HttpResponse('<a href="/">Return back to homepage</a><br> <h1>Room not found</h1>')


@permission_required('registration.view_buyer', login_url='restricted/')
def user_details(request):
    if request.method == "GET":
        Room_list = Room.objects.all()
        buyer_list = Buyer.objects.all()
        owner_list = Owner.objects.all()
        context_variable = {
            'detail': Room_list,
            'buyer': buyer_list,
            'owner': owner_list,
        }
        print(context_variable)
        return render(request, 'details.html', context_variable)


def home_restricted(request):
    return render(request, 'restricted.html')

def add_to_cart(request, id):
    user_profile = get_object_or_404(User, username=request.user)
    rooms = Room.objects.get(id=id)
    order_item, status = Book.objects.get_or_create(room=rooms)
    user_order, status = Reserve.objects.get_or_create(user=user_profile)
    user_order.rooms.add(order_item)
    if status:
        user_order.save()

    return redirect(reverse('carts'))

@permission_required('rooms.delete_room', login_url='restricted/')
def delete(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()
    return redirect("/")

