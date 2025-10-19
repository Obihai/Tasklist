from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def task_list(request):
    return HttpResponse("Task list placeholder — auth and templates coming soon")
