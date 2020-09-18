from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('SDDD/',views.SanketListView.as_view()),
    path('',RedirectView.as_view(url='SDDD/')),
    path('SDDD/<int:pk>',views.SanketDetailView.as_view()),
]
