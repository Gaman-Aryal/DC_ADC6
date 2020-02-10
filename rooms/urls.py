from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('photoupload_form/', upload),
    path('photoupload_form/restricted/', home_restricted),
    path('Photo_upload_result/', uploadphoto),
    path('update_form/<int:pk>', update_form),
    path('update_form/restricted/', home_restricted),
    path('update_form/update/<int:pk>/', update),
    path('delete/<int:pk>',delete),
    path('delete/restricted/', home_restricted),
    path('download/<int:pk>/', download_image, name='download'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
