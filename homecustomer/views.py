from django.shortcuts import render

# Create your views here.
from .models import CustomerFeedback, StayConnected
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NewsLetterForm, FeedbackForm

# class home(ListView):
# 	queryset = CustomerFeedback.objects.all()
# 	template_name = 'index.html'

class NewsLetter(CreateView):
	form_class = NewsLetterForm
	template_name = 'index.html'
	success_url = '/'

	def get_context_data(self, **kwargs):
		kwargs['object_list'] = CustomerFeedback.objects.all()
		return super(NewsLetter, self).get_context_data(**kwargs)

class NewsLetterListView(LoginRequiredMixin, ListView):
	template_name = "NewsfeedList.html"
	queryset = StayConnected.objects.all()

class PushCustomerFeedback(LoginRequiredMixin, CreateView):
	form_class = FeedbackForm
	template_name = 'feedback.html'
	success_url = 'resortadmin/feedback/'

class CustomerFeedbackListView(LoginRequiredMixin, ListView):
	template_name = "CustomerFeedbackList.html"
	queryset = CustomerFeedback.objects.all()

class CustomerFeedbackDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomerFeedback
    template_name = 'CustomerFeedback_confirm_delete.html'
    success_url = '/resortadmin/feedback/'