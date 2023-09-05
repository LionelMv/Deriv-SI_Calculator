from django.urls import path
from . import views

urlpatterns = [
  path('', views.Indice, name='calculator-home'),
  path('about/', views.about, name='calculator-about')
]
