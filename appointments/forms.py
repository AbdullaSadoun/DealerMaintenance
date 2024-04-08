from django import forms
from .models import Appointment
from vehicles.models import Vehicle
from services.models import Service

class AppointmentForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), required=True)
    service = forms.ModelChoiceField(queryset=Service.objects.all(), required=True)
    appointment_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    appointment_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))

    class Meta:
        model = Appointment
        fields = ['vehicle', 'service', 'appointment_date', 'appointment_time']
