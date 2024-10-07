from django.urls import path
from .views import *

app_name = 'accounts'


urlpatterns = [
    path('',Home,name='Home'),
     path('contact/',contact,name='contact'),
     path('create-appointment/',createappointment,name='createappointment'),
    path('update-appointment/',updateappointment,name='updateappointment'),
    path('delet-appointment/',deletappointment,name='deletappointment'),
    path('payment/', create_visa_card, name='VisaCard_create'),
    path('error/', erro_visa, name='erro_visa'),


]


