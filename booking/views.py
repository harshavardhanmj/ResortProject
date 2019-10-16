import datetime
from django.shortcuts import render, render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView, DeleteView
from .models import Booking, Contact
from roomsactivities.models import Room, RoomCheck
from .forms import BookingForm, ContactForm


# Create your views here.

class MainView(TemplateView):
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        booking_form = BookingForm(self.request.GET or None)
        contact_form = ContactForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['booking_form'] = booking_form
        context['contact_form'] = contact_form
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Room.objects.all()
        return super(MainView, self).get_context_data(**kwargs)


class BookingFormView(FormView):
    form_class = BookingForm
    template_name = 'booking.html'
    success_url = '/booking'

    def post(self, request, *args, **kwargs):
        booking_form = self.form_class(request.POST)
        contact_form = ContactForm()
        if booking_form.is_valid():
            booking_form.save()
            RoomName = request.POST.get("room_type")
            Rooms = request.POST.get("rooms")
            startdate = request.POST.get("datepicker1")
            enddate = request.POST.get("datepicker2")
            date1 = datetime.datetime.strptime(startdate, '%m/%d/%Y')
            date2 = datetime.datetime.strptime(enddate, '%m/%d/%Y')
            while (1):
                DateAppend = str(date1)
                roomchec = RoomName + DateAppend
                RoomObj = Room.objects.get(room_name__iexact=RoomName)
                RoomGlobalAvail = RoomObj.room_availability
                RoomChecObj = RoomCheck.objects.filter(room_name__iexact=roomchec)
                if RoomChecObj.exists():
                    RoomChecObj1 = RoomCheck.objects.get(room_name__iexact=roomchec)
                    RoomAcc = RoomChecObj1.room_accomadete
                    if RoomAcc >= int(Rooms):
                        RoomChecObj1.room_accomadete = RoomAcc - int(Rooms)
                        RoomChecObj1.save()
                else:
                    obj = RoomCheck.objects.create(
                        room_name=roomchec,
                        room_accomadete=RoomGlobalAvail
                    )
                    obj.room_accomadete = obj.room_accomadete - int(Rooms)
                    obj.save()

                date1 += datetime.timedelta(days=1)
                if (date1 > date2):
                    break;
            return self.render_to_response(self.get_context_data(success=True))
        else:
            return self.render_to_response(self.get_context_data(booking_form=booking_form, contact_form=contact_form))

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Room.objects.all()
        return super(BookingFormView, self).get_context_data(**kwargs)


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'booking.html'
    success_url = '/booking'

    def post(self, request, *args, **kwargs):
        contact_form = self.form_class(request.POST)
        booking_form = BookingForm()
        if contact_form.is_valid():
            contact_form.save()
            return self.render_to_response(self.get_context_data(success=False))
        else:
            return self.render_to_response(self.get_context_data(booking_form=booking_form, contact_form=contact_form))

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Room.objects.all()
        return super(ContactFormView, self).get_context_data(**kwargs)


class ContactListView(LoginRequiredMixin, ListView):
    template_name = "contactlist.html"
    queryset = Contact.objects.all()


class ContactDetailView(LoginRequiredMixin, DetailView):
    template_name = "contactdetail.html"
    queryset = Contact.objects.all()


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'Contact_confirm_delete.html'
    success_url = '/resortadmin/ContactCustomer/'


class BookingListView(LoginRequiredMixin, ListView):
    template_name = "bookinglist.html"
    queryset = Booking.objects.all()


class BookingDetailView(LoginRequiredMixin, DetailView):
    template_name = "bookingdetail.html"
    queryset = Booking.objects.all()


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'Booking_confirm_delete.html'
    success_url = '/resortadmin/checkbookings/'


class AdminView(LoginRequiredMixin, TemplateView):
    template_name = "admin.html"
