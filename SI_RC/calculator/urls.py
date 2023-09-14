from django.urls import path
from . import views

urlpatterns = [
  path('calculator/', views.Indice, name='calculator-home'),
  path('calculator/about/', views.about, name='calculator-about')
]
