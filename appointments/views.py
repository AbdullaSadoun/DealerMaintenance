#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AppointmentForm

def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/schedule_appointment.html', {'form': form})


# mechanic stuff
from .models import Appointment
from django.utils.timezone import datetime  # use timezone-aware datetime

def view_appointments(request):
    today = datetime.today()
    appointments = Appointment.objects.filter(appointment_date__gte=today).order_by('appointment_date', 'appointment_time')
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})

