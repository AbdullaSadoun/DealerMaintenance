from django.db import models

# Create your models here.

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    transmission_type = models.CharField(max_length=50)
    oil_type = models.CharField(max_length=50)
    tire_size = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
