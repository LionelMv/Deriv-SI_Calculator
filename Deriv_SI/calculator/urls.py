from django.urls import path
from . import views

urlpatterns = [
  path('', views.Indice, name='calculator-home'),
]
