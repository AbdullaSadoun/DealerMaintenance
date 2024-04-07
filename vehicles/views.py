from django.shortcuts import render

# Create your views here.

from .models import Vehicle

def list_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/list_vehicles.html', {'vehicles': vehicles})
