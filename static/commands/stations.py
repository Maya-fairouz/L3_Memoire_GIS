# from django.core.management.base import BaseCommand
# from main.models import Stations

# class Command(BaseCommand):
#     help = 'Generates vehicle objects in the database'

#     def handle(self, *args, **options):
#         Stations.objects.create(
#                 name_station= 'station 0',
#                 latitude_station=36.24781,
#                 longitude_station=6.56996
#             )
           
            
        
#         print(f"{Stations().objects.count()} vehicles now in the database")
         
#         for station in Stations().objects.all():
#          print(station.id,station.name,staion.latitude,station.longitude)
         
#         # for vehicle in Vehicle.objects.all():
#         #  vehicle.delete()


# #         import random
# # from django.core.management.base import BaseCommand
# # from core.models import Vehicle

# # class Command(BaseCommand):
# #     help = 'Generates vehicle objects in the database'

# #     def handle(self, *args, **options):
# #         NUM_VEHICLES_TO_GENERATE = 2

# #         latitudes = [36.24781, 36.35842]
# #         longitudes = [6.56996, 6.60571]

# #         for vehicle in Vehicle.objects.all():
# #          vehicle.delete()    

# #         for i in range(NUM_VEHICLES_TO_GENERATE):
# #             id = "t_" + str(i)
# #             latitude = latitudes[i]
# #             longitude = longitudes[i]
# #             Vehicle.objects.create(latitude=latitude, longitude=longitude)            
        
# #         print(f"{Vehicle.objects.count()} vehicles now in the database")
         
# #         for vehicle in Vehicle.objects.all():
# #          print(vehicle.latitude,vehicle.longitude)