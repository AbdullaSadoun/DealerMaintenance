"""
URL configuration for mycarproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.shortcuts import redirect #to avoid the error of no URL to redirect to
# from vehicles.views import home  # Import the home view (no longer needed as i made a homepage in main app)
from mycarproject.views import home  # Adjust the import path according to your project structure
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),  # Update this line to use the home view for vehicles
    #path('', home, name='home'),  # Make sure this points to the new home view
    #path('', include('vehicles.urls')),
    #path('', include('services.urls')),
    #path('', lambda request: redirect('list_vehicles', permanent=False)),  # to redirect to the list_vehicles page
    #path('appointments/', include('appointments.urls')),  # Include the appointments app URLs


    path('', views.home, name='home'),  # Assuming a home view exists
    path('vehicles/', include('vehicles.urls')),
    path('services/', include('services.urls')),
    path('appointments/', include('appointments.urls')),
    # about us page
    path('about_us/', views.about_us, name='about_us'),

]
