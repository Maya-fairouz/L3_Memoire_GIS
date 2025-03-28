import traci
import random
import time
from django.core.management.base import BaseCommand
from main.models import Vehicle

sumo_binary = "sumo-gui"
sumo_cmd = [sumo_binary, "-c", "C:/Users/ETS MESSAHEL/Desktop/2023-04-03-14-57-47/osm.sumocfg"]

traci.start(sumo_cmd)
print("Connected to SUMO")

class Command(BaseCommand):
    help = 'Simulate vehicle movement'

    def handle(self, *args, **options):
        print("Simulating..")
        # Define the range of latitude and longitude variation
        while traci.simulation.getMinExpectedNumber() > 0:
            traci.simulationStep()
            # x, y = traci.vehicle.getPosition('t_0')

            position_cartesian = traci.vehicle.getPosition('t_0')

            # Convert the cartesian coordinates to latitude and longitude
            longitude,latitude = traci.simulation.convertGeo(position_cartesian[0], position_cartesian[1])

            
            for vehicle in Vehicle.objects.all() :
                vehicle.latitude =latitude
                vehicle.longitude =longitude
                vehicle.save()
            
                
            time.sleep(1)

        traci.close()

        
# import traci
# import random
# import time
# from django.core.management.base import BaseCommand
# from core.models import Vehicle

# sumo_binary = "sumo-gui"
# sumo_cmd = [sumo_binary, "-c", "C:/Users/ETS MESSAHEL/Desktop/2023-04-03-14-57-47/osm.sumocfg"]

# traci.start(sumo_cmd)
# print("Connected to SUMO")

# class Command(BaseCommand):
#     help = 'Simulate vehicle movement'

#     def handle(self, *args, **options):
#         # Define the range of latitude and longitude variation
#         while traci.simulation.getMinExpectedNumber() > 0:
#             traci.simulationStep()

#             for i in range(20):
#                 vehicle_id = "t_" + str(i)
#                 position_cartesian = traci.vehicle.getPosition(vehicle_id)

#                 # Convert the cartesian coordinates to latitude and longitude
#                 longitude, latitude = traci.simulation.convertGeo(position_cartesian[0], position_cartesian[1])

#                 # Store the position of the vehicle in the database
#                 vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
#                 vehicle.latitude = latitude
#                 vehicle.longitude = longitude
#                 vehicle.save()

#             time.sleep(1)

#         traci.close()


