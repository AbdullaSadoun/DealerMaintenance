'''
this is the models file for the vehicle service application
    
'''
from prettytable import PrettyTable
from datetime import datetime

class Service:
    def __init__(self, service_id, service_name, estimated_time, estimated_labour_cost):
        self.service_id = service_id
        self.service_name = service_name
        self.estimated_time = estimated_time
        self.estimated_labour_cost = estimated_labour_cost
class Vehicle:
    def __init__(self, vehicle_id, make, model, year, fuel_type, transmission_type, oil_type, tire_size):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.transmission_type = transmission_type
        self.oil_type = oil_type
        self.tire_size = tire_size

    '''def view_Vehicle(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Transmission Type: {self.transmission_type}")
        print(f"Oil Type: {self.oil_type}")
        print(f"Tire Size: {self.tire_size}")
    '''
    '''def view_Vehicle(self): no longer needed
        table = PrettyTable()
        table.field_names = ["Vehicle ID", "Make", "Model", "Year", "Fuel Type", "Transmission Type", "Oil Type", "Tire Size"]
        table.add_row([self.vehicle_id, self.make, self.model, self.year, self.fuel_type, self.transmission_type, self.oil_type, self.tire_size])
        print(table)'''

class Mechanic:
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

    def add_appointment(self, day, time, car_owner, service_requested, car_model):
        # Check if the time is within the mechanic's working hours and not during his break time
        if (time < "9:00" or time > "17:00" or (time >= "13:00" and time < "14:00")):
            print("The mechanic is not available at this time.")
            return

        # Check if the time slot is free
        if not self.is_time_slot_free(day, time):
            print("The mechanic is already booked at this time.")
            return

        appointment = {
            "day": day,
            "time": time,
            "car_owner": car_owner,
            "service_requested": service_requested,
            "car_model": car_model,
        }
        self.schedule.append(appointment)

    def view_schedule_for_day(self, day):
        table = PrettyTable()
        table.field_names = ["Day", "Time", "Car Owner", "Service Requested", "Car Model"]
        
        for appointment in self.schedule:
            if appointment['day'] == day:
                table.add_row([appointment['day'], appointment['time'], appointment['car_owner'], appointment['service_requested'], appointment['car_model']])
        
        print(table)












def delete_vehicle_by_id(vehicle_id, car_models): 
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
            fuel_type = input("Enter the fuel type of the car: ")
            transmission_type = input("Enter the transmission type of the car: ")
            oil_type = input("Enter the oil type of the car: ")
            tire_size = input("Enter the tire size of the car: ")
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

    '''
    with open('vehicle_table.txt', 'w') as f:
        for vehicle in car_models:
            f.write(f"{vehicle.vehicle_id},{vehicle.make},{vehicle.model},{vehicle.year},{vehicle.fuel_type},{vehicle.transmission_type},{vehicle.oil_type},{vehicle.tire_size}\n")

    with open('availserv.txt', 'w') as f:
        for service in services:
            f.write(f"{service.service_id},{service.service_name},{service.service_price}\n")'''

    if car_models:  # Only write to the file if the car_models list is not empty
        with open('vehicle_table.txt', 'w') as f:
            for vehicle in car_models:
                f.write(f"{vehicle.vehicle_id},{vehicle.make},{vehicle.model},{vehicle.year},{vehicle.fuel_type},{vehicle.transmission_type},{vehicle.oil_type},{vehicle.tire_size}\n")

    if services:  # Only write to the file if the services list is not empty
        with open('availserv.txt', 'w') as f:
            for service in services:
                f.write(f"{service.service_id},{service.service_name},{service.service_price}\n")
    
    return








def car_owner_interface(car_models, services):
    # Step 1: Ask the user for their car details
    carowner_make = input("Enter your car make: ").upper()
    carowner_model = input("Enter your car model: ").upper()

    # Step 2: Check if the car model is in the car_models list
    '''if car_model not in car_models:
        print("Sorry, we do not have any services available for your car.")
        return'''
    
    '''for car_models.make in car_models:
        if car_make == car_models.make and car_makesmodel == car_models.model:
            print("We have your car model in our database.")
            break
        else:
            print("Sorry, we do not have any services available for your car.")
            return'''
    
    for car_models in car_models:
        if carowner_make == car_models.make and carowner_model == car_models.model:
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

    # Step 4: If the user chooses to call a mechanic for other services, handle that option
    # This will depend on your implementation

    # Step 5: If the user chooses a service, calculate the estimated cost
    estimated_cost = chosen_service.estimated_labour_cost

    # Step 6: Print a "receipt" with the cost, schedule, date of request, and vehicle info and customer info
    customer_name = input("Please enter your name: ")
    customer_email = input("Please enter your email: ")
    customer_phone_number = input("Please enter your phone number: ")
    customer_info = PrettyTable()
    customer_info.field_names = ["Customer's Name", "Contact Email", "Contact Phone No."]
    customer_info.add_row([customer_name, customer_email, customer_phone_number])
    print(customer_info)
 
    receipt = PrettyTable()
    receipt.field_names = ["Car Make", "Car Model", "Service", "Estimated Cost", "Date of Request"]
    receipt.add_row([carowner_make, carowner_model, chosen_service.service_name, estimated_cost, datetime.now().strftime("%Y-%m-%d")])
    print(receipt)










        
    

'''class Part:
    def __init__(self, part_id, part_name, cost):
        self.part_id = part_id
        self.part_name = part_name
        self.cost = cost

class VehicleService:
    def __init__(self, vehicle_service_id, vehicle_id, service_id, cost, parts_required):
        self.vehicle_service_id = vehicle_service_id
        self.vehicle_id = vehicle_id
        self.service_id = service_id
        self.cost = cost
        self.parts_required = parts_required
'''