"""
Car Maintenance software that estimates the cost for a car's maintenance based 
on the car's model, age and mileage. Then it schedules a maintenance appointment
for the mechanic, it would show what his schedule looks like for the day.

The software should have the following features:
- The software should ask the user whether they are an admin, a mechanic or a car owner
- If the user is an admin, they should be able to add, update or delete car models and their tables
- If the user is a mechanic, they should be able to view the list of car models
- If the user is a car owner, they should be able to enter the car's model, year and mileage
- The software should then estimate the cost for the car's maintenance based on the car's model, age and mileage
- The software should display the estimated cost to the user
- The software should schedule a maintenance appointment for the car depending on the estimated time to maintain
- The software should display the maintenance appointment to the user

Available Maintenance Services:
- Oil Change and Lubrication Service
- Tire Services
- Brake Services
- Battery Inspection and Replacement
- Engine Diagnostic and Performance
- These will be the deafult options, the admin should be able to add, update or delete these services

The software should have the following tables:
- Car Models
- Maintenance Services
- Maintenance Schedule
- The tables should be stored in a database
- The software should be able to create the database if it does not exist
- The software should be able to connect to the database
- The software should be able to create the tables if they do not exist
- The software should be able to insert, update or delete records in the tables
- The software should be able to select records from the tables
- The software should be able to drop the tables
- The software should be able to drop the database
- The software should be able to close the connection to the database

incorprate PEP8 styling standards
"""
# Your code here
# import the models file
from models import Vehicle, Service
from models import delete_vehicle_by_id, view_all_vehicles, admin_interface, delete_service_by_id, view_all_services

def read_data_from_files(car_models, services):
    car_models = []
    services = []

    try:
        with open('vehicles.txt', 'r') as f:
            for line in f:
                vehicle_id, make, model, year, fuel_type, transmission_type, oil_type, tire_size = line.strip().split(',')
                car_models.append(Vehicle(vehicle_id, make, model, int(year), fuel_type, transmission_type, oil_type, tire_size))

        with open('availserv.txt', 'r') as f:
            for line in f:
                service_id, service_name, estimated_time, estimated_labour_cost = line.strip().split(',')
                services.append(Service(service_id, service_name, estimated_time, float(estimated_labour_cost)))
    except FileNotFoundError:
        print("Data files not found. Starting with empty lists.")

    return car_models, services

# reading the file to see if there are priopr records
car_models, services = read_data_from_files()

print("Welcome to the Car Maintenance software!") # welcome message
# Ask the user whether they are an admin, a mechanic or a car owner
user_type = int(input("Are you an car owner(1), a mechanic(2) or an admin(3)? "))

if user_type == 3: # user is an admin
    print("You are an admin!!")
    print("Enter Password")
    password = input("Enter your password: ")
    while password != "admin":
        print("Invalid password")
        password = input("Enter your password: ")

    print("Welcome Admin!")
    admin_interface(car_models, services)

elif user_type == 2: # user is a mechanic
    print("You are a mechanic!!")
    #prompt to enter the day they wanna see the schedule for
    print("What day would you like to see the schedule for?")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    print("5. Friday")
    print("6. Exit")
    mechanic_choice = input("Enter your choice: ")
    if mechanic_choice == "1":
        print("You chose to see the schedule for Monday.")
        #display the schedule for that day


    elif mechanic_choice == "2":
        print("You chose to see the schedule for Tuesday.")
        #display the schedule for that day
    
    
    elif mechanic_choice == "3":
        print("You chose to see the schedule for Wednesday.")
        #display the schedule for that day

    elif mechanic_choice == "4":
        print("You chose to see the schedule for Thursday.")
        #display the schedule for that day

    elif mechanic_choice == "5":
        print("You chose to see the schedule for Friday.")
        #display the schedule for that day

    


