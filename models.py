'''
this is the models file for the vehicle service application

has the following classes:
- Service
- Vehicle
- Mechanic

has the following functions:
- view_schedule_for_day
- delete_vehicle_by_id
- view_all_vehicles
- delete_service_by_id
- view_all_services
- view_all_appointments
- view_appointments_for_day
- admin_interface
- read_data_from_files
- car_owner_interface

'''

from prettytable import PrettyTable
from datetime import datetime

class Service: # class for the services that can be offered
    def __init__(self, service_id, service_name, estimated_time, estimated_labour_cost):
        self.service_id = service_id
        self.service_name = service_name
        self.estimated_time = estimated_time
        self.estimated_labour_cost = estimated_labour_cost
class Vehicle: # class for the vehicles that can be serviced
    def __init__(self, vehicle_id, make, model, year, fuel_type, transmission_type, oil_type, tire_size):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.transmission_type = transmission_type
        self.oil_type = oil_type
        self.tire_size = tire_size
class Mechanic: # class for the mechanic (his name, contact, schedule)
    def __init__(self, mechanic_id, mechanic_name, mechanic_email, mechanic_phone):
        self.mechanic_id = mechanic_id
        self.mechanic_name = mechanic_name
        self.mechanic_email = mechanic_email
        self.mechanic_phone = mechanic_phone
        self.schedule = []

    def is_time_slot_free(self, day, time):
        for appointment in self.schedule:
            if appointment['day'] == day and appointment['time'] == time:
                return False
        return True

    def find_next_available_time(self, start_day):
        # Define the mechanic's working hours and days
        working_hours = ["9:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00"]
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        # Start checking from the given day
        for day in days_of_week[days_of_week.index(start_day):]:
            for time in working_hours:
                if self.is_time_slot_free(day, time):
                    return day, time

        # If no time slot is free, return None
        return None, None

    def add_appointment(self, day, car_owner, service_requested, car_model):
        # Find the next available time slot
        day, time = self.find_next_available_time(day)

        # If no time slot is free, print a message and return
        if time is None:
            print("The mechanic is not available in the following days.")
            return

        appointment = {
            "day": day,
            "time": time,
            "car_owner": car_owner,
            "service_requested": service_requested,
            "car_model": car_model,
        }
        self.schedule.append(appointment)

        # Return the day and time of the appointment
        return day, time

def view_schedule_for_day(mechanic_schedule, day): # searches for the schedule for a given day from the mechanic schedule
    table = PrettyTable()
    table.field_names = ["Day", "Time", "Car Owner", "Service Requested", "Car Model"]
    
    for appointment in mechanic_schedule:
        if appointment['day'] == day:
            table.add_row([appointment['day'], appointment['time'], appointment['car_owner'], appointment['service_requested'], appointment['car_model']])
    
    print(table)

def delete_vehicle_by_id(vehicle_id, car_models): # 
    for i in range(len(car_models)):
        if car_models[i].vehicle_id == vehicle_id:
            del car_models[i]
            print(f"Vehicle with ID {vehicle_id} has been deleted.")
            return
    print(f"No vehicle found with ID {vehicle_id}.")
    return

def view_all_vehicles(car_models):
    table = PrettyTable()
    table.field_names = ["Vehicle ID", "Make", "Model", "Year", "Fuel Type", "Transmission Type", "Oil Type", "Tire Size"]
    for vehicle in car_models:
        table.add_row([vehicle.vehicle_id, vehicle.make, vehicle.model, vehicle.year, vehicle.fuel_type, vehicle.transmission_type, vehicle.oil_type, vehicle.tire_size])
    print(table)
    return


def delete_service_by_id(service_id, services):
    for i in range(len(services)):
        if services[i].service_id == service_id:
            del services[i]
            print(f"Service with ID {service_id} has been deleted.")
            return
    print(f"No service found with ID {service_id}.")
    return

def view_all_services(services):
    table = PrettyTable()
    table.field_names = ["Service ID", "Service Name", "Estimated Time", "Estimated Labour Cost"]
    for service in services:
        table.add_row([service.service_id, service.service_name, service.estimated_time, service.estimated_labour_cost])
    print(table)

def view_all_appointments(mechanic_schedule):
    table = PrettyTable()
    table.field_names = ["Day", "Time", "Car Owner", "Service Requested", "Car Model"]
    for appointment in mechanic_schedule:
        table.add_row([appointment['day'], appointment['time'], appointment['car_owner'], appointment['service_requested'], appointment['car_model']])
    print(table)

def view_appointments_for_day(mechanic_schedule, day):
    table = PrettyTable()
    table.field_names = ["Day", "Time", "Car Owner", "Service Requested", "Car Model"]
    for appointment in mechanic_schedule:
        if appointment['day'] == day:
            table.add_row([appointment['day'], appointment['time'], appointment['car_owner'], appointment['service_requested'], appointment['car_model']])
    print(table)


def read_data_from_files():
    car_models = []
    services = []
    schedule = []

    try: # try to open the files containting the data
        with open('vehicle_table.txt', 'r') as f:
            for line in f:
                vehicle_id, make, model, year, fuel_type, transmission_type, oil_type, tire_size = line.strip().split(',')
                car_models.append(Vehicle(vehicle_id, make, model, int(year), fuel_type, transmission_type, oil_type, tire_size))

        with open('availserv.txt', 'r') as f:
            for line in f:
                service_id, service_name, estimated_time, estimated_labour_cost = line.strip().split(',')
                services.append(Service(service_id, service_name, estimated_time, float(estimated_labour_cost)))
        
        with open('mechanic1.txt', 'r') as f:
            for line in f:
                day, time, car_owner, service_requested, car_model = line.strip().split(',')
                appointment = {'day': day, 'time': time, 'car_owner': car_owner, 'service_requested': service_requested, 'car_model': car_model}
                schedule.append(appointment)
    except FileNotFoundError: # if the an error is encountered print the following message
        print("Data files not found. Starting with empty lists.")

    return car_models, services, schedule

def admin_interface(car_models, services):
    while True:
        print("1. Add to Car Models Table")
        print("2. Delete from Car Models Table")
        print("3. View Car Models Table")
        print("4. Add to Services Table")
        print("5. Delete from Services Table")
        print("6. View Services Table")
        print("7. Exit")
        try:
            admin_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if admin_choice == 1:
            # code to add to Car Models Table
            print("You chose to add to the Car Models Table.")
            #prompt to enter the car model details
            make = input("Enter the make of the car: ").upper()
            model = input("Enter the model of the car: ").upper()
            year = input("Enter the year of the car: ")
            fuel_type = input("Enter the fuel type of the car: ").upper()
            transmission_type = input("Enter the transmission type of the car: ").upper()
            oil_type = input("Enter the oil type of the car: ").upper()
            tire_size = input("Enter the tire size of the car: ").upper()
            vehicle_id = len(car_models) + 1
            #insert the car model details into the car model table by adding the record to the table
            vehicle = Vehicle(vehicle_id, make, model, year, fuel_type, transmission_type, oil_type, tire_size)
            car_models.append(vehicle)

        elif admin_choice == 2:
            # code to delete from Car Models Table
            vehicle_id = int(input("Enter the ID of the vehicle you want to delete: "))
            delete_vehicle_by_id(vehicle_id, car_models)
            
        elif admin_choice == 3:
            view_all_vehicles(car_models)
            
        elif admin_choice == 4:
            # code to add to Services Table
            print("You chose to add to the Maintenance Services Table.")
            #prompt to enter the service details
            service_name = input("Enter the name of the service: ")
            estimated_time = input("Enter the estimated time for the service: ")
            estimated_labour_cost = input("Enter the estimated labour cost for the service: ")
            #insert the service details into the maintenance services table by adding the record to the table
            service_id = len(services) + 1
            service = Service(service_id, service_name, estimated_time, estimated_labour_cost)
            services.append(service)

        elif admin_choice == 5:
            # code to delete from Services Table
            service_id = int(input("Enter the ID of the service you want to delete: "))
            delete_service_by_id(service_id, services)

        elif admin_choice == 6:
            # code to view Services Table
            view_all_services(services)
            
        elif admin_choice == 7:
            print("Exiting admin interface.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

   
    if car_models:  # Only write to the file if the car_models list is not empty
        with open('vehicle_table.txt', 'w') as f:
            for vehicle in car_models:
                f.write(f"{vehicle.vehicle_id},{vehicle.make},{vehicle.model},{vehicle.year},{vehicle.fuel_type},{vehicle.transmission_type},{vehicle.oil_type},{vehicle.tire_size}\n")

    if services:  # Only write to the file if the services list is not empty
        with open('availserv.txt', 'w') as f:
            for service in services:
                f.write(f"{service.service_id},{service.service_name},{service.estimated_time},{service.estimated_labour_cost}\n")
    
    return

def car_owner_interface(car_models, services, mechanic):
    # Step 1: Ask the user for their car details
    carowner_make = input("Enter your car make: ").upper()
    carowner_model = input("Enter your car model: ").upper()

    # Step 2: Check if the car model is in the car_models list
    for car_model in car_models:
        if carowner_make == car_model.make and carowner_model == car_model.model:
            print("We have your car model in our database.")
            break
    else:  # This else clause corresponds to the for loop, not the if statement
        print("Sorry, we do not have any services available for your car.")
        return

    # Step 3: If the car model is in the list, display available services
    print("Here are the available services for your car:")
    
    for i, service in enumerate(services, start=1):
        print(f"{i}. {service.service_name}")
    service_choice = int(input("Enter the number of the service you want to choose: "))
    chosen_service = services[service_choice - 1]

    # Step 4: If the user chooses a service, calculate the estimated cost
    estimated_cost = chosen_service.estimated_labour_cost

    # Step 5: Book an appointment with the mechanic
    start_day = input("Enter the start day for the service (e.g., 'Monday'): ")
    day, time = mechanic.add_appointment(start_day, carowner_make + " " + carowner_model, chosen_service.service_name, carowner_model)

    # Step 6: Print a "receipt" with the cost, schedule, date of request, and vehicle info and customer info
    customer_name = input("Please enter your name: ")
    customer_email = input("Please enter your email: ")
    customer_phone_number = input("Please enter your phone number: ")
    customer_info = PrettyTable()
    customer_info.field_names = ["Customer's Name", "Contact Email", "Contact Phone No."]
    customer_info.add_row([customer_name, customer_email, customer_phone_number])
    print(customer_info)
 
    receipt = PrettyTable()
    receipt.field_names = ["Car Make", "Car Model", "Service", "Estimated Cost", "Date of Request", "Appointment Day", "Appointment Time"]
    receipt.add_row([carowner_make, carowner_model, chosen_service.service_name, estimated_cost, datetime.now().strftime("%Y-%m-%d"), day, time])
    print(receipt)

    # Step 7: Write the new appointment to the 'mechanic1.txt' file
    with open('mechanic1.txt', 'a') as f:
        f.write(f"{day},{time},{customer_name},{chosen_service.service_name},{carowner_make + ' ' + carowner_model}\n")









