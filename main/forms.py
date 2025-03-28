from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ObstaclesForm(ModelForm):
    class Meta:
        model = Obstacle
        fields = ['location', 'description', 'image','reported_by','status']
        
class TeamAssignmentForm(forms.ModelForm):
    class Meta:
        model = TeamAssignment
        fields = ['team', 'user']
                
class IncidentForm(ModelForm):
    class Meta:
        model = Incident
        fields = ['vehicle','type', 'description', 'reported_by','location']

# class TeamForm(ModelForm):
#     class Meta:
#         model = Team
#         fields = ['name','user1','user2','user3']

class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ['vehicle','type','date','team']

class StatusForm(ModelForm):
    class Meta:
        model = StatusV
        fields = ['vehicle','status','reported_by','description']

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['line','vehicle','departure','arrival','frequency']



