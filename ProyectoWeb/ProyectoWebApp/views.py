from django.http import HttpResponse
from django.shortcuts import render

from carro.views import Carro


# Create your views here.
def home(request):
    carro = Carro(request)
    return render(request, 'ProyectoWebApp/home.html')












