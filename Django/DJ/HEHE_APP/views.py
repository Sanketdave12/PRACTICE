from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!!")

def sd(request):
    return render(request,"home.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")
