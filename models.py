'''
this is the models file for the vehicle service application
    
'''
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

class Service:
    def __init__(self, service_id, service_name, estimated_time):
        self.service_id = service_id
        self.service_name = service_name
        self.estimated_time = estimated_time

class Part:
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