from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rooms.models import Room
import json


@csrf_exempt
def view_get_post_room(request):
    print("What's the request => ", request.method)
    if request.method == "GET":
        room = Room.objects.all()
        print("QuerySet objects => ", room)
        list_of_rooms = list(room.values("Room_owner", "Room_price", "Room_location", "pub_date","Room_desc", "Room_phnumber"))
        print("List of rooms objects => ", list_of_rooms)
        dictionary_name = {
            "room": list_of_rooms
        }
        return JsonResponse(dictionary_name)


    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>", python_dictionary_object)
        print("Python dictionary type=>", type(python_dictionary_object))
        print(python_dictionary_object['Room_owner'])
        print(python_dictionary_object['Room_price'])
        print(python_dictionary_object['Room_phnumber'])
        print(python_dictionary_object['pub_date'])
        print(python_dictionary_object['Room_desc'])
        print(python_dictionary_object['Room_location'])
        Room.objects.create(Room_owner=python_dictionary_object['Room_owner'],
                            Room_price=python_dictionary_object['Room_price'],
                            Room_phnumber=python_dictionary_object['Room_phnumber'],
                            pub_date=python_dictionary_object['pub_date'],
                            Room_desc=python_dictionary_object['Room_desc'],
                            Room_location=python_dictionary_object['Room_location'],
                            )
        return JsonResponse({
            "message": "Successfully posted!!"
        })
    else:
        return HttpResponse("error occured")

@csrf_exempt 
def view_Rooms_pagination(request,PAGENO,SIZE):
    skip=SIZE*(PAGENO -1)
    room=Room.objects.values() [skip:(PAGENO*SIZE)]
     
    roomdictonary={
        "room":list(room.values("Room_owner","Room_phnumber","pub_date","Room_desc","Room_location","Room_price"))
        }
    return JsonResponse(roomdictonary)

@csrf_exempt
def view_getByID(request, ID):
    print("What's the request =>", request.method)
    if request.method == "GET":
        room = Room.objects.get(id=ID)
        print(type(room.Room_desc))
        return JsonResponse({
            "id": room.id,
            "Room_owner": room.Room_owner,
            "Room_price": room.Room_price,
            "pub_date": room.Room_price,
            "Room_location": room.Room_location,
            "Room_desc": room.Room_desc,
            "Room_phnumber" : room.Room_phnumber,

        })

    else:
        return JsonResponse({
            "message": "error occured"
        })

@csrf_exempt
def get_update_delete(request,ID):
    print("What's the request =>",request.method)
    room = Room.objects.get(id=ID)
    if request.method == "GET":
        print(type(room.Room_desc))
        return JsonResponse({
            "id": room.id,
            "Room_owner": room.Room_owner,
            "Room_price": room.Room_price,
            "pub_date": room.pub_date,
            "Room_location": room.Room_location,
            "Room_desc": room.Room_desc,
            "Room_phnumber" : room.Room_phnumber,
        })
    elif request.method=="DELETE":
        room = Room.objects.get(id = ID)
        room.delete()
        return JsonResponse({
            "message":"Successfully deleated!!"
        })

    elif request.method == "PUT":
        update = json.loads(request.body)
        room.Room_owner=update['Room_owner']
        room.Room_price=update['Room_price']
        room.Room_desc=update['Room_desc']
        room.pub_date=update['pub_date']
        room.Room_location=update['Room_location']
        room.Room_phnumber=update['Room_phnumber']
        room.save()
        return JsonResponse({
            "message":"Successfully Updated!!"})