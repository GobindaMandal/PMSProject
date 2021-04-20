from django.http import HttpResponse
from django.shortcuts import render
from . models import Destination


# Create your views here.

def index(request):
   return render(request, 'index.html')

def buying(request):
   return render(request, 'buying.html')

def selling(request):
   return render(request, 'selling.html')

def contacts(request):
   return render(request, 'contacts.html')
