from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = [
			'room_name',
			'room_cost',
			'room_description',
			'room_thumImg',
			'room_img1',
			'room_img2',
			'room_img3',
			'room_img4',
			'room_img5',
			'room_facilities',
			'room_availability',
			'room_accomadete',
		]

	def __init__(self, *args, **kwargs):
		super(RoomForm, self).__init__(*args, **kwargs)
		self.fields['room_name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_cost'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_description'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_thumImg'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_img1'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_img2'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_img3'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_img4'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_img5'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_facilities'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_availability'].widget.attrs.update({'class' : 'form-control'})
		self.fields['room_accomadete'].widget.attrs.update({'class' : 'form-control'})