import datetime
from django import forms
from .models import Booking, Contact
from roomsactivities.models import Room, RoomCheck


class BookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = [
			'adults',
			'rooms',
			'room_type',
			'phone_number',
			'datepicker1',
			'datepicker2',
			'email'
		]

	def clean(self):
		roomNo = self.cleaned_data.get("rooms")
		roomType = self.cleaned_data.get("room_type")
		checkin = self.cleaned_data.get("datepicker1")
		checkout = self.cleaned_data.get("datepicker2")
		date1 = datetime.datetime.strptime(str(checkin), '%Y-%m-%d')
		date2 = datetime.datetime.strptime(str(checkout), '%Y-%m-%d')
		tempdate = datetime.datetime.now().date()
		curdate = datetime.datetime.strptime(str(tempdate), '%Y-%m-%d')
		if(date1>date2):
			raise forms.ValidationError("Improper Date")
		if(date1<curdate):
			raise forms.ValidationError("Improper Date")
		if(date2<curdate):
			raise forms.ValidationError("Improper Date")
		while (1):
			fieldName = roomType + str(date1)
			qs = RoomCheck.objects.filter(room_name__iexact=fieldName)
			#print(qs)
			if qs.exists():
				qs1 = RoomCheck.objects.get(room_name__iexact=fieldName)
				if(qs1.room_accomadete < int(roomNo)):
					#print("yes")
					raise forms.ValidationError("Room Not available on this date")
					break;
			date1 += datetime.timedelta(days=1)
			if(date1>date2):
				break;
		return


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = [
			'Name',
			'Email',
			'Message',
		]