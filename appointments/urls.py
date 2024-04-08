from django.urls import path
from . import views

urlpatterns = [
    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
]
