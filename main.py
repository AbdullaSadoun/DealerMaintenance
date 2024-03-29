##
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
- Diagnosis
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
# Importing the modules
# Importing the models methods
from models import (Vehicle, Service, Mechanic, read_data_from_files,
                    view_all_vehicles, admin_interface, view_all_services,
                    car_owner_interface, view_all_appointments,
                    view_schedule_for_day)
from prettytable import PrettyTable

# "magic numberless"
CAR_OWNER = 1
MECHANIC = 2
ADMIN = 3

# Reading the file to see if there are prior records from previous runs
car_models, services, mechanic_schedule = read_data_from_files()

# Create an instance mechanic
mechanic = Mechanic(1, "John", "jb@dal.ca", "902-123-4567")

# Welcome message
print("Welcome to the Car Maintenance software!") 

# Ask the user whether they are an admin, a mechanic or a car owner
user_type = int(input("Are you a car owner(1), a mechanic(2) or an admin(3)? "))

if user_type == ADMIN:  # User is an admin
    print("You are an admin!!")
    
    password = input("Enter your password(Hint: admin): ")
    while password != "admin":
        print("Invalid password")
        password = input("Enter your password: ")

    print("Welcome Admin!")
    admin_interface(car_models, services)

elif user_type == MECHANIC:  # User is a mechanic
    print("You are a mechanic!!")
    # Prompt to enter the day they wanna see the schedule for
    print("What day would you like to see the schedule for?")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    print("5. Friday")
    print("6. Exit")

    mechanic_choice = input("Enter your choice: ")
    day_mapping = {"1": "Monday", "2": "Tuesday", "3": "Wednesday", 
                   "4": "Thursday", "5": "Friday"}
    if mechanic_choice in day_mapping:
        print(f"You chose to see the schedule for {day_mapping[mechanic_choice]}.")
        view_schedule_for_day(mechanic_schedule, day_mapping[mechanic_choice])  

elif user_type == CAR_OWNER:  # User is a car owner
    car_owner_interface(car_models, services, mechanic)

