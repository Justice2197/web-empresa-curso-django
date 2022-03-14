from django.urls import path
from . import views

urlpatterns = [
  #Path Contact
  path('', views.contact, name="contact"),
]