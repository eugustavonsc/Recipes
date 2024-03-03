from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return render(request, 'recipes/home.html')
def sobre(request):
    return render(request, "recipes/sobre.html")
def contato(request):
    return render(request, "recipes/contato.html")


# Create your views here.
