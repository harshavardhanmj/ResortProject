from django.contrib import admin

# Register your models here.
from .models import Room, RoomCheck

myModels = [Room, RoomCheck]

admin.site.register(myModels)