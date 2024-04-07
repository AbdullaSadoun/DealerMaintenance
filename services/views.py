from django.shortcuts import render

# Create your views here.
from .models import Service

def list_services(request):
    services = Service.objects.all()
    return render(request, 'services/list_services.html', {'services': services})
