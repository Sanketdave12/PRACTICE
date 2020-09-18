from django.contrib import admin
from django.urls import path,include
from REAL_APP import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('sd/',views.sdListView.as_view()),
    path('sd/<int:pk>',views.sdDetailView.as_view()),
    path('',RedirectView.as_view(url= "sd/")),
    path("",views.home),
    
]
