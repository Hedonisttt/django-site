from django.shortcuts import render
from .models import Task



def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, "main/about.html")


def catalog(request):
    tasks = Task.objects.all()
    return render(request, 'main/catalog.html', {'tit': 'Каталог Товаров', 'tasks': tasks})

def supp(request):
    return render(request, "main/support.html")