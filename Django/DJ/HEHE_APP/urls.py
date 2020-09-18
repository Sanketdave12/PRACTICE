from django.contrib import admin
from django.urls import path,include
from HEHE_APP import views

urlpatterns = [
    
    path("contact/",views.contact ),
    path("about/",views.about ),
    path("", views.sd),
    path('admin/', admin.site.urls),
] 
