
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
for vehicle in Vehicle.objects.all():
         vehicle.delete()    

# Define the range of latitude and longitude variation
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()


    vehicle_ids = traci.vehicle.getIDList()

    # Print the IDs to the console
    for vehicle_id in vehicle_ids:
    # get the vehicle's position
         
        position_cartesian = traci.vehicle.getPosition(vehicle_id)
        longitude,latitude = traci.simulation.convertGeo(position_cartesian[0], position_cartesian[1])
        speed = traci.vehicle.getSpeed(vehicle_id)
        tNextBusStop=traci.vehicle.getStopState(vehicle_id)
        
        vehicle = Vehicle.objects.filter(name=vehicle_id).first()

        # if vehicle_id =='pt_tram_Tramway_de_Constantine_â:0.0':
        #      print(vehicle_id ,':',tNextBusStop)
        # If the vehicle already exists, update its data
        if vehicle:
            vehicle.latitude = latitude
            vehicle.longitude = longitude
            vehicle.speed = speed
            vehicle.save()

        # If the vehicle does not exist, create a new row in the database
        else:
            Vehicle.objects.create(name=vehicle_id, latitude=latitude, longitude=longitude)


        # print('##',vehicle_id,'. next stop :' ,tNextBusStop)
    # time.sleep(1)                                     
traci.close()
