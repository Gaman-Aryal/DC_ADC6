from rooms.models import Room
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.http import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import permission_required, login_required
from wsgiref.util import FileWrapper
import mimetypes, os, re


@permission_required('rooms.add_room', login_url='restricted/')
def upload(request):
    return render(request, 'upload.html')


@permission_required('rooms.delete_room', login_url='restricted/')
def delete(request, pk):
    room = Room.objects.get(pk=pk)
    room.delete()
    return redirect("/")


def uploadphoto(request):
    if request.method == "POST":
        uploaded_image = request.FILES['image']
        fssobj = FileSystemStorage()
        filename = fssobj.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fssobj.url(filename)

        room = Room(file=uploaded_image_url,
                    Room_owner=request.POST['owner_name'],
                    Room_location=request.POST['location'],
                    Room_phnumber=request.POST['phone_number'],
                    Room_price=request.POST['price'],
                    pub_date=request.POST['pub_date'],
                    Room_desc=request.POST['desc'])
        room.save()
        return HttpResponse(
            'You have successfully uploaded the room photo with its detail<br><br><a href="/">Go to homepage</a>')
    else:
        return render(request, 'upload.html')


@permission_required('rooms.change_room', login_url='restricted/')
def update_form(request, pk):
    room = Room.objects.get(pk=pk)
    return render(request, 'edit.html', {'room': room})


def update(request, pk):
    room = Room.objects.get(pk=pk)
    print()
    if request.method == "POST":
        updated_image = request.FILES['image']
        fssobj1 = FileSystemStorage()
        filename1 = fssobj1.save(updated_image.name, updated_image)
        updated_image_url = fssobj1.url(filename1)

        room.file = updated_image_url
        room.Room_owner = request.POST['owner_name']
        room.Room_location = request.POST['location']
        room.Room_phnumber = request.POST['phone_number']
        room.Room_price = request.POST['price']
        room.pub_date = request.POST['pub_date']
        room.Room_desc = request.POST['desc']
        room.save()
        return redirect("/")

    else:
        return HttpResponse('<h2>UPDATE FAILED</h2>')


def download_image(request, pk):
    img = Room.objects.get(pk=pk)
    wrapper = FileWrapper(img.file)
    content_type = mimetypes.guess_type(str(img.file))[0]
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(str(img.file))
    response['Content-Disposition'] = "attachment; filename=%s" % img.file
    return response


def home_restricted(request):
    return render(request, 'restricted.html')
