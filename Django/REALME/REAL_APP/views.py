from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import sd
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'home.html')

class sdListView(ListView):
    model = sd

@method_decorator(login_required,name="dispatch")
class sdDetailView(DetailView):
    model = sd