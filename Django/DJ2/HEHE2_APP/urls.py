
from django.contrib import admin
from django.urls import path
from HEHE2_APP import views

urlpatterns = [
    path('contact/',views.contact),
    path('about/',views.about),
    path('',views.home),

]


