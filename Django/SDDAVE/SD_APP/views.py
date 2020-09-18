from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import SDDD
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

def home(request):
    return render(request,'base.html')

class SanketListView(ListView):
    model = SDDD

class SanketDetailView(DetailView):
    model = SDDD
