'''
this is the models file for the vehicle service application
    
'''
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
            make = input("Enter the make of the car: ")
            model = input("Enter the model of the car: ")
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

    with open('vehicles.txt', 'w') as f:
        for vehicle in car_models:
            f.write(f"{vehicle.vehicle_id},{vehicle.make},{vehicle.model},{vehicle.year},{vehicle.fuel_type},{vehicle.transmission_type},{vehicle.oil_type},{vehicle.tire_size}\n")

    with open('availserv.txt', 'w') as f:
        for service in services:
            f.write(f"{service.service_id},{service.service_name},{service.service_price}\n")
    
    return











def delete_vehicle_by_id(vehicle_id, car_models): 
    for i in range(len(car_models)):
        if car_models[i].vehicle_id == vehicle_id:
            del car_models[i]
            print(f"Vehicle with ID {vehicle_id} has been deleted.")
            return
    print(f"No vehicle found with ID {vehicle_id}.")
    return

def view_all_vehicles(car_models):
    for vehicle in car_models:
        vehicle.view_Vehicle()
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
    for service in services:
        service.view_Service()
    return


        
    

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