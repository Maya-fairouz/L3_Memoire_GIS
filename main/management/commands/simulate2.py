import traci
import random
import time
from django.core.management.base import BaseCommand
from main.models import Vehicle

# Start the TraCI simulation
sumo_binary = "sumo-gui"
sumo_cmd = [sumo_binary, "-c", "C:/Users/ETS MESSAHEL/Sumo/2023-05-08-21-05-58/osm.sumocfg"]

traci.start(sumo_cmd)
print("Connected to SUMO")

bus_stops = traci.getBusStops()

# Print the names of all bus stops
for bus_stop in bus_stops:
    print(bus_stop["name"])
# Stop the TraCI simulation
traci.close()
