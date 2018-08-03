from django import forms
from .models import StayConnected, CustomerFeedback

class NewsLetterForm(forms.ModelForm):
	class Meta:
		model = StayConnected
		fields = [
			'customer_email',
		]

	def clean_customer_email(self):
		email = self.cleaned_data.get("customer_email")
		qs = StayConnected.objects.filter(customer_email__iexact=email)
		if qs.exists():
			raise forms.ValidationError("Email Already Registered")
		return email

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = CustomerFeedback
		fields = [
			'cutomer_name',
			'customer_feedback'
		]

	def __init__(self, *args, **kwargs):
		super(FeedbackForm, self).__init__(*args, **kwargs)
		self.fields['cutomer_name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['customer_feedback'].widget.attrs.update({'class' : 'form-control'})