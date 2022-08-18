from django.shortcuts import render
from .models import Cattleya
from .models import Dendrobium

# Create your views here.
def home(request):
    return render(request, 'home.html')
def cattleya(request):
    mylist = Cattleya.objects.all()
    return render(request, 'cattleya.html', {'mylist':mylist})
def dendrobium(request):
    dendr = Dendrobium.objects.all()
    return render(request, 'dendrobium.html', {'dendr':dendr})
