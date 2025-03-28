
from django.db import models
from django.contrib.auth.models import User,Group
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='', upload_to='profile_pic')
    name = models.CharField(max_length=50 , default='')
    email=models.EmailField(default='')
    phone= models.IntegerField()
    adress = models.TextField(null=True)
    def __str__(self):
        return f'{self.user.username} Profile'
    



class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , default='')
    latitude = models.FloatField()
    longitude = models.FloatField()
    speed = models.FloatField(default=0)
    def __str__(self):
        return self.name
        
       

class Stations(models.Model):
    id_station = models.AutoField(primary_key=True)
    name_station = models.CharField(max_length=51 , default='')
    lat_station = models.FloatField()
    long_station = models.FloatField()


class Agents(models.Model):
    user= models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField( max_length=50, null =True)
    phone=models.CharField( max_length=50, null =True)
    email=models.CharField( max_length=50, null =True)
    date_created = models.DateField( auto_now_add=True, null=True)


class Obstacle(models.Model):
    STATUS =( 
        ('Fixed','Fixed'),
        ('Pending','Pending'),

    )
    location = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='obstacle_images/', null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    reported_by = models.CharField(max_length=100, null=True)
    status = models.CharField( null=True, choices=STATUS )
   
    # ****************************************

class Room(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
        
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=10000)

    # **********************************************

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Incident(models.Model):
    STATUS =( 
        ('Fixed','Fixed'),
        ('Pending','Pending'),

    )

    INCIDENT_TYPES = [
        ('Fire', 'Fire'),
        ('Collision','Collision'),
        ('Signal Failure', 'Signal Failure'),
        ('Track Obstruction', 'Track Obstruction'),
        ('Vandalism', 'Vandalism'),
        ('Equipment Malfunction', 'Equipment Malfunction'),
        ('Emergency Situation', 'Emergency Situation'),
        # Add more incident types as needed
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    reported_by = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    status = models.CharField( null=True, choices=STATUS )



class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class TeamAssignment(models.Model):
    
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    date = models.DateField()
    team = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.vehicle} - {self.type} - {self.date}"


class StatusV(models.Model):
    STATUS=[
        ('Pending','Pending'),
        ('Fixed','Fixed')
    ]
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    status = models.CharField(null=True, choices=STATUS )
    date = models.DateTimeField(auto_now_add=True, null=True)
    reported_by = models.CharField(max_length=100, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.vehicle} - {self.status} - {self.date}"

class Schedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    line = models.CharField(max_length=100, null=True)

    departure= models.TimeField()
    arrival = models.TimeField()
    frequency = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
     