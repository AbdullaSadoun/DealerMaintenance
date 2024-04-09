#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment


def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            appointment = form.save()
            return redirect('appointment_success', appointment_id=appointment.id)
    else:
        form = AppointmentForm()
    return render(request, 'appointments/schedule_appointment.html', {'form': form})


# mechanic stuff
from .models import Appointment
from django.utils.timezone import datetime  # use timezone-aware datetime

def view_appointments(request):
    today = datetime.today()
    # appointments = Appointment.objects.filter(appointment_date__gte=today).order_by('appointment_date', 'appointment_time')
    appointments = Appointment.objects.all().order_by('appointment_date', 'appointment_time') # Order by date first, then by time
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})


# to display the success page:: 
def appointment_success(request, appointment_id):
    return render(request, 'appointment_success.html', {'appointment_id': appointment_id})

# for pdf and success stuff
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Appointment

def download_pdf(request, appointment_id):
    # Fetch the appointment from the database
    appointment = Appointment.objects.get(id=appointment_id)

    # Create the HttpResponse object with the appropriate headers
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="appointment_{appointment_id}_confirmation.pdf"'

    # Create the PDF object using the response object as its "file"
    p = canvas.Canvas(response)

    # Draw the PDF content here, for example:
    p.drawString(100, 800, f"Appointment ID: {appointment.id}")
    p.drawString(100, 780, f"Service: {appointment.service}")
    p.drawString(100, 760, f"Date: {appointment.appointment_date}")
    p.drawString(100, 740, f"Time: {appointment.appointment_time}")

    # close pdf object
    p.showPage()
    p.save()
    return response

