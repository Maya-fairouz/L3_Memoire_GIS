
import traci
import random
import time
from django.core.management.base import BaseCommand
from main.models import Vehicle

sumo_binary = "sumo-gui"
sumo_cmd = [sumo_binary, "-c", "C:/Users/ETS MESSAHEL/Sumo/2023-05-08-21-05-58/osm.sumocfg"]

traci.start(sumo_cmd)
print("Connected to SUMO")


print("Simulating..")
# Define the range of latitude and longitude variation
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()


    vehicle_ids = traci.vehicle.getIDList()

    # Print the IDs to the console
    for vehicle_id in vehicle_ids:
    # get the vehicle's position
        position_cartesian = traci.vehicle.getPosition(vehicle_id)
        longitude,latitude = traci.simulation.convertGeo(position_cartesian[0], position_cartesian[1])

        vehicle = Vehicle.objects.filter(name=vehicle_id).first()

        # If the vehicle already exists, update its data
        if vehicle:
            
            vehicle.latitude = latitude
            vehicle.longitude = longitude
            vehicle.save()

        # If the vehicle does not exist, create a new row in the database
        else:
            Vehicle.objects.create(name=vehicle_id, latitude=latitude, longitude=longitude)

        
    # time.sleep(1)                                     
traci.close()
# *****************************************************************************************************
# import traci
# import random
# import time
# from django.core.management.base import BaseCommand
# # from main.models import Vehicle

# sumo_binary = "sumo-gui"
# sumo_cmd = [sumo_binary, "-c", "C:/Users/ETS MESSAHEL/Sumo/2023-05-08-21-05-58/osm.sumocfg"]

# traci.start(sumo_cmd)
# # traci.simulation.setParameter("scale", "0.1")
# print("Connected to SUMO")

# # class Command(BaseCommand):
    
      
#     # def handle(self, *args, **options):
# print("Simulating..")



# while traci.simulation.getMinExpectedNumber() > 0:
#     traci.simulationStep()

#     # departed_vehicles = traci.simulation.getDepartedNumber()
#     # arrived_vehicles = traci.simulation.getArrivedNumber()

#     # # Compute the number of vehicles currently in the simulation
#     # current_vehicles = departed_vehicles - arrived_vehicles

#     # # Print the result to the console
#     # print("There are currently", current_vehicles, "vehicles in the simulation")

            
#     # print("working ..")
#     vehicle_ids = traci.vehicle.getIDList()

#     # Print the IDs to the console
#     for vehicle_id in vehicle_ids:
#     # get the vehicle's position
#         position = traci.vehicle.getPosition(vehicle_id)
#         # get the vehicle's speed
#         speed = traci.vehicle.getSpeed(vehicle_id)
#         # get the vehicle's route
#         route = traci.vehicle.getRoute(vehicle_id)
#         # get the vehicle's type
#         vehicle_type = traci.vehicle.getTypeID(vehicle_id)
#         # print the information for this vehicle
#         print("Vehicle ID:", vehicle_id)
#         print("Position:", position)
#         print("Speed:", speed)
#         print("Route:", route)
#         print("Vehicle Type:", vehicle_type)
#         # # for vehicle in Vehicle.objects.all() :
#         # #     vehicle.latitude =latitude
#         # #     vehicle.longitude =longitude
#         # #     vehicle.save()
    
        
#     time.sleep(1)                                     

# traci.close()

