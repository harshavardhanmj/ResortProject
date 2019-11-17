import datetime
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from roomsactivities.models import Room, RoomCheck
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import RegexValidator
import karix
from karix.rest import ApiException
from karix.configuration import Configuration
from karix.api_client import ApiClient

# Create your models here.
class Booking(models.Model):
	adults = models.IntegerField(null=True,blank=True)
	rooms = models.IntegerField(null=True,blank=True)
	email = models.EmailField(max_length=320,null=True,blank=True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True, null=True)
	room_type = models.CharField(max_length=120,null=True,blank=True)
	datepicker1 = models.DateField(auto_now=False, auto_now_add=False,null=True)
	datepicker2 = models.DateField(auto_now=False, auto_now_add=False,null=True)

	def __str__(self):
		return self.email

def post_save_booking_receiver(sender, instance, created, *args, **kwargs):
	if created:
		subject = 'Coorg Jungleway Booking Confirmation'
		from_email = settings.DEFAULT_FROM_EMAIL
		recipient_list = [instance.email, from_email]
		message = f'Payment Required for confirmation'
		html_message = f'<h1>Thank You for choosing us</h1><br/><h3>Your Booking ID is {instance.id} and confirmation will be made upon the same by us shortly through call.</h3>'
		sent_mail= send_mail(
				subject, 
				message, 
				from_email, 
				recipient_list, 
				fail_silently=False, 
				html_message=html_message)
		sent_mail = True
		# sms_message = "Coorg Jungleway Booking Confirmation. Payment Required for confirmation. Thank You for choosing us. Your Booking ID is " + str(instance.id)
		# number = "+91" + str(instance.phone_number)
		# config = Configuration()
		# config.username = '89de2a7e-5bed-41a1-bce1-47be10d042891'
		# config.password = '39f9dd68-d96f-4ea1-b80f-74e828b2f9451'
		# api_instance = karix.MessageApi(api_client=ApiClient(configuration=config))
		# message = karix.CreateMessage(source="+919845320802", destination=[number], text=sms_message)
		#api_response = api_instance.send_message(message=message)
post_save.connect(post_save_booking_receiver, sender=Booking)

def post_delete_booking_receiver(sender, instance, *args, **kwargs):
	RoomName = instance.room_type
	Rooms = instance.rooms
	startdate = instance.datepicker1
	enddate = instance.datepicker2
	date1 = startdate
	date2 = enddate
	while(1):
		DateAppend = str(date1)
		roomchec = RoomName + DateAppend + " 00:00:00"
		RoomObj = Room.objects.get(room_name__iexact=RoomName)
		RoomGlobalAvail = RoomObj.room_availability
		RoomChecObj = RoomCheck.objects.filter(room_name__iexact=roomchec)
		if RoomChecObj.exists():
			RoomChecObj1 = RoomCheck.objects.get(room_name__iexact=roomchec)
			RoomAcc = RoomChecObj1.room_accomadete
			RoomChecObj1.room_accomadete = RoomAcc+int(Rooms)
			RoomChecObj1.save()
			if RoomAcc != RoomGlobalAvail:
				RoomChecObj1.delete()
		date1 += datetime.timedelta(days=1)
		if(date1>date2):
			break;
post_delete.connect(post_delete_booking_receiver, sender=Booking)

class Contact(models.Model):
	Name = models.CharField(max_length=220,null=True,blank=True)
	Email = models.EmailField(max_length=320,null=True,blank=True)
	Message = models.TextField(max_length=1000,null=True,blank=True)

	def __str__(self):
		return self.Email