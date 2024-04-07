from django.db import models

# Create your models here.

class Service(models.Model):
    service_name = models.CharField(max_length=200)
    estimated_time = models.CharField(max_length=100)  # Consider changing to IntegerField if it's always in minutes
    estimated_labour_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.service_name
