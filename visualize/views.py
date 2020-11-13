from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

def visualize_home(request):
    return HttpResponse('---- visualize_home - 1 -------')
