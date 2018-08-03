from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Room
from .forms import RoomForm
# Create your views here.

class RoomListView(ListView):
    template_name = "cuisines.html"
    queryset = Room.objects.all()

class RoomDetailView(DetailView):
    template_name = "roomdetails.html"
    queryset = Room.objects.all()

    def get_context_data(self, *args, **kwargs):
    	context = super(RoomDetailView, self).get_context_data(*args, **kwargs)
    	#print(self.kwargs['slug'])
    	room_object = Room.objects.get(slug__iexact=self.kwargs['slug'])
    	ac = False
    	wifi = False
    	tv = False
    	hotwater = False
    	bf = False
    	service = False
    	paper = False
    	carrent = False
    	balcony = False
    	if "ac" in room_object.room_facilities:
    		ac = True
    	if "wifi" in room_object.room_facilities:
    		wifi = True
    	if "tv" in room_object.room_facilities:
    		tv = True
    	if "hotwater" in room_object.room_facilities:
    		hotwater = True
    	if "bf" in room_object.room_facilities:
    		bf = True
    	if "service" in room_object.room_facilities:
    		service = True
    	if "paper" in room_object.room_facilities:
    		paper = True
    	if "carrent" in room_object.room_facilities:
    		carrent = True
    	if "balcony" in room_object.room_facilities:
    		balcony = True
    	context['ac'] = ac
    	context['wifi'] = wifi
    	context['tv'] = tv
    	context['hotwater'] = hotwater
    	context['bf'] = bf
    	context['service'] = service
    	context['paper'] = paper
    	context['carrent'] = carrent
    	context['balcony'] = balcony
    	context['person'] = room_object.room_accomadete
    	return context

class RoomCreateView(LoginRequiredMixin, CreateView):
    form_class = RoomForm
    template_name = 'AdminRoom.html'
    success_url = '/resortadmin/room/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.room_thumImg = self.request.FILES['room_thumImg']
        obj.room_img1 = self.request.FILES['room_img1']
        obj.room_img2 = self.request.FILES['room_img2']
        obj.room_img3 = self.request.FILES['room_img3']
        obj.room_img4 = self.request.FILES['room_img4']
        obj.room_img5 = self.request.FILES['room_img5']
        obj.save()
        return super(RoomCreateView, self).form_valid(form)

class RoomAdminListView(LoginRequiredMixin, ListView):
    template_name = 'AdminRoomList.html'
    queryset = Room.objects.all()

class RoomAdminDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'Room_confirm_delete.html'
    success_url = '/resortadmin/room/'