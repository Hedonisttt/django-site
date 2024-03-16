from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm



def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, "main/about.html")


def catalog(request):
    tasks = Task.objects.all()
    return render(request, 'main/catalog.html', {'tit': 'Каталог Товаров', 'tasks': tasks})

def supp(request):
    return render(request, "main/support.html")

def create(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


        else:
            error = 'Форма не Верная'



    form = TaskForm()
    context = {
        'form' : form,
        'error': error
    }
    return render(request, "main/create.html", context)