from django.contrib import admin

# Register your models here.
from .models import CustomerFeedback, StayConnected

myModels = [CustomerFeedback, StayConnected]

admin.site.register(myModels)