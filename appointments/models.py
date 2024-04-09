from django.db import models

# Create your models here.
from vehicles.models import Vehicle
from services.models import Service

class Appointment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.vehicle} - {self.service} on {self.appointment_date} at {self.appointment_time}"


