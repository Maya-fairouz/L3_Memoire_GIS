from django.core.management.base import BaseCommand
from main.models import Vehicle

class Command(BaseCommand):
    help = 'Generates vehicle objects in the database'

    def handle(self, *args, **options):
        NUM_VEHICLES_TO_GENERATE = 10
        for vehicle in Vehicle.objects.all():
         vehicle.delete()    

        # for i in range(NUM_VEHICLES_TO_GENERATE):
        #     Vehicle.objects.create(
        #         name= 'bich',
        #         latitude=36.24781,
        #         longitude=6.56996
        #     )
            
        
        print(f"{Vehicle.objects.count()} vehicles now in the database")
         
        for vehicle in Vehicle.objects.all():
         print(vehicle.id,vehicle.name,vehicle.latitude,vehicle.longitude)
         
        # for vehicle in Vehicle.objects.all():
        #  vehicle.delete()


#         import random
# from django.core.management.base import BaseCommand
# from core.models import Vehicle

# class Command(BaseCommand):
#     help = 'Generates vehicle objects in the database'

#     def handle(self, *args, **options):
#         NUM_VEHICLES_TO_GENERATE = 2

#         latitudes = [36.24781, 36.35842]
#         longitudes = [6.56996, 6.60571]

#         for vehicle in Vehicle.objects.all():
#          vehicle.delete()    

#         for i in range(NUM_VEHICLES_TO_GENERATE):
#             id = "t_" + str(i)
#             latitude = latitudes[i]
#             longitude = longitudes[i]
#             Vehicle.objects.create(latitude=latitude, longitude=longitude)            
        
#         print(f"{Vehicle.objects.count()} vehicles now in the database")
         
#         for vehicle in Vehicle.objects.all():
#          print(vehicle.latitude,vehicle.longitude)