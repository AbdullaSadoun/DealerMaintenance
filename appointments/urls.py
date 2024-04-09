from django.urls import path
from . import views
from .views import download_pdf

urlpatterns = [
    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),

    # for success stuff:
    path('appointments/success/<int:appointment_id>/', views.appointment_success, name='appointment_success'),
    path('appointments/pdf/<int:appointment_id>/', views.download_pdf, name='download_pdf'),
    path('pdf/<int:appointment_id>/', download_pdf, name='download_pdf'),
]
