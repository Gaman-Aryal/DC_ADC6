from django.contrib import admin
from .models import Reserve
from .models import Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Reserve)