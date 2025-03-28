from django.contrib import admin
from . import models


# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id','name','latitude','longitude','speed')
admin.site.register(models.Vehicle , VehicleAdmin) 

class StationAdmin(admin.ModelAdmin):
    list_display = ('id_station','name_station','lat_station','long_station')
admin.site.register(models.Stations , StationAdmin) 


class AgentAdmin(admin.ModelAdmin):
    list_display = ('user','name','phone','email')
admin.site.register(models.Agents,AgentAdmin)


admin.site.register(models.Obstacle)
admin.site.register(models.Incident)
admin.site.register(models.Room)
admin.site.register(models.Team)
admin.site.register(models.Notification)
admin.site.register(models.TeamAssignment)
admin.site.register(models.StatusV)
admin.site.register(models.Maintenance)
admin.site.register(models.Schedule)
admin.site.register(models.Profile)
# *********************************

class MessageAdmin(admin.ModelAdmin):
    list_display = ('value','date','user','room')
admin.site.register(models.Message,MessageAdmin)
# *******************