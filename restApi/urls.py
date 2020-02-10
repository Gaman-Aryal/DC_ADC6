from django.urls import path
from .views import *

urlpatterns = [
    path('room/',view_get_post_room),
    path('room/<int:ID>/',get_update_delete),
    path('roompage/PAGENO=<int:PAGENO>/SIZE=<int:SIZE>',view_Rooms_pagination)

]