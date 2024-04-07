from django.urls import path
from . import views

urlpatterns = [
    path('vehicles/', views.list_vehicles, name='list_vehicles'),
]
