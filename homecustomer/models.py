from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

#User = settings.AUTH_USER_MODEL

class CustomerFeedback(models.Model):
	cutomer_name = models.CharField(max_length=120,null=True,blank=True)
	customer_feedback = models.TextField(max_length=1500,null=True,blank=True)
	
	def __str__(self):
		return self.cutomer_name

class StayConnected(models.Model):
	customer_email = models.EmailField(null=True,blank=True)
	
	def __str__(self):
		return self.customer_email