from django.contrib import admin

# Register your models here.
from .models import Booking, Contact

myModels = [Booking, Contact]

admin.site.register(myModels)