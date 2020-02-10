from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import homepage, logout_view, search,user_details,home_restricted, add_to_cart, home_restricted, delete

urlpatterns = [
    path('', homepage,name='homepage'),
    path('users_details/',user_details,name='user_details'),
    path('users_details/restricted/',home_restricted,name='user_details'),
    path('logout/', homepage, name="homepage"),
    path('logout_redirect/', logout_view , name="logout" ),
    path('search/', search),
    path('search/reserve/cart/<int:id>/', add_to_cart),
    path('search/rooms/delete/<int:pk>',delete),
    path('search/rooms/delete/restricted/', home_restricted),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)