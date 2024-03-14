import django.http
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    context = {
        'name': 'bilibili~',
    }
    return render(request, 'book/index.html', context=context)
