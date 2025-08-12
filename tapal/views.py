from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def newtapal(request):
    return render(request, 'newtapal.html')


def list_tapal(request):
    return render(request, 'listtapal.html')
