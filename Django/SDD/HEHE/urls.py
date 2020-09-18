from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('notice/',views.NoticeListView.as_view()),
    path('notice/<int:pk>',views.NoticeDetailView.as_view()),
    path('',RedirectView.as_view(url="notice/")),

]