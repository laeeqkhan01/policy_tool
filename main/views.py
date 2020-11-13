from django.shortcuts import render
from django.http      import HttpResponse

# Create your views here.

def main_home(request):
  #return HttpResponse('------ main_home - 1 ----------')
  return render(request, 'main/main_home.html')
