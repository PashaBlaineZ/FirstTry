from django.shortcuts import render
from .models import Books
from django.http import HttpResponse


def index(request):
    databass = Books.objects.all()
    return render(request, 'main/index.html', {'title':'Главная страница сайта', 'databass':databass})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    return render(request, 'main/create.html')

def findbook(request):
    return render(request, 'main/find.html')

def returnbook(request):
    return render(request, 'main/return.html')

def takebook(request):
    return render(request, 'main/take.html')

def randombook(request):
    return render(request, 'main/random.html')

