from django.urls import path
from .           import views

urlpatterns = [
  path('', views.visualize_home, name='visualize_home'),
]
