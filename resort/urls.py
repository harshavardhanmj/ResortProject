"""resort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from homecustomer.views import NewsLetter, NewsLetterListView, PushCustomerFeedback, CustomerFeedbackDeleteView, CustomerFeedbackListView
from roomsactivities.views import RoomListView, RoomDetailView, RoomCreateView, RoomAdminListView, RoomAdminDeleteView
from booking.views import MainView, BookingFormView, ContactDeleteView, ContactFormView, BookingDeleteView, ContactListView, ContactDetailView, BookingListView, BookingDetailView, AdminView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', NewsLetter.as_view(), name='NewsLetter'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html'), name="about"),
    url(r'^gallery/$', TemplateView.as_view(template_name = 'gallery.html'), name="gallery"),
    url(r'^resortadmin/$', AdminView.as_view(), name="admin"),
    url(r'^cuisines/$', RoomListView.as_view(), name='cuisines'),
    url(r'^cuisines/(?P<slug>[\w-]+)/$', RoomDetailView.as_view(), name='cuisinesdetails'),
    url(r'^booking/$', MainView.as_view(), name='booking'),
    url(r'^roombooking/$', BookingFormView.as_view(), name='roombooking'),
    url(r'^contact/$', ContactFormView.as_view(), name='contact'),
    url(r'^resortadmin/room/$', RoomAdminListView.as_view(), name='listroom'),
    url(r'^resortadmin/room/add/$', RoomCreateView.as_view(), name='createroom'),
    url(r'^resortadmin/room/(?P<pk>\d+)/$', RoomAdminDeleteView.as_view(), name='RoomAdminDeleteView'),
    url(r'^resortadmin/feedback/$', CustomerFeedbackListView.as_view(), name='CustomerFeedbackListView'),
    url(r'^resortadmin/feedback/add/$', PushCustomerFeedback.as_view(), name='feedback'),
    url(r'^resortadmin/deletefeedback/(?P<pk>\d+)/$', CustomerFeedbackDeleteView.as_view(), name='CustomerFeedbackDeleteView'),
    url(r'^resortadmin/ContactCustomer/$', ContactListView.as_view(), name='contactCustomer'),
    url(r'^resortadmin/ContactCustomer/(?P<pk>\d+)/$', ContactDetailView.as_view(), name='contactCustomerDetails'),
    url(r'^resortadmin/DeleteContactCustomer/(?P<pk>\d+)/$', ContactDeleteView.as_view(), name='ContactDeleteView'),
    url(r'^resortadmin/NewsfeedMail/$', NewsLetterListView.as_view(), name='Newsfeed'),
    url(r'^resortadmin/checkbookings/$', BookingListView.as_view(), name='checkbookings'),
    url(r'^resortadmin/deletebooking/(?P<pk>\d+)/$', BookingDeleteView.as_view(), name='BookingDeleteView'),
    url(r'^resortadmin/checkbookings/(?P<pk>\d+)/$', BookingDetailView.as_view(), name='checkbookingsDetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)