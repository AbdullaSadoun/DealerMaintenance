from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.list_services, name='list_services'),
]
