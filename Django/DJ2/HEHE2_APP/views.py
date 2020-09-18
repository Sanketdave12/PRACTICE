from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from HEHE2_APP.models import notice
# Create your views here.
def home(request):
    return render(request,"master.html")

def about(request):
    return render(request,"About.html")

def contact(request):
    return render(request,"contact.html")


class NoticeListView(ListView):
    model=  notice

class NoticeDetailView(DetailView):
    model=  notice