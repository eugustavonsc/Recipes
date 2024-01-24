from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return render(request, 'home.html')
def sobre(request):
    return HttpResponse("Sobre")
def contato(request):
    return HttpResponse("Contato")


# Create your views here.
