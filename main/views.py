from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from main.models import Vehicle, Stations
from . import models
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import * 


# from .decoraters import unauthenticated_user,allowed_users,admin_only


# Create your views here.

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
          form.save()
          username= form.cleaned_data.get('username')
          messages.success(request, 'Account has been created for '+username)


          return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST': 
        username=request.POST.get('username')
        password=request.POST.get('password')
       
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request,user)
            return redirect('home')
        else:
            print("FAILED")
            messages.info(request, "Username OR password is inccorect  , Try again ..")

    context = {}
    return render(request,'login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
# @admin_only
def home(request):
    username =request.user.username
    notifications =Notification.objects.all()
    rooms = Room.objects.all()
    context = {'vehicles': list(Vehicle.objects.values('id','name','latitude','longitude','speed')),'username': username,'notifications':notifications, 'rooms':rooms}
    return render(request, 'home.html', context)
# returning the position of all the vehicles 
# in the db as 
#json data to the client side 

def vehicle_positions(request):
    vehicles= Vehicle.objects.all().values('id','name','latitude','longitude','speed')
    return JsonResponse({'vehicles': list(vehicles)})

def station_positions(request):
    stations = Stations.objects.all().values('name_station', 'lat_station', 'long_station')
    return JsonResponse({'stations': list(stations)})

def redX(request):
    # incidents = Incident.objects.all()
    obstacles = Obstacle.objects.all().values('location','description','status')
    return JsonResponse({'obstacles': list(obstacles)})

def redX2(request):
    incidents = Incident.objects.all().values('location','description')
    return JsonResponse({'incidents': list(incidents)})



def opManager(request):
    context = {}
    return render(request,'actors/opmanager.html',context)

def trainController(request):
    context = {}
    return render(request,'actors/traincontroller.html',context)

def fieldAgent(request):
    context = {}
    return render(request,'actors/fieldagent.html',context)

def depotManager(request):
    context = {}
    return render(request,'actors/depotmanager.html',context)

def maitenanceAgent(request):
    context = {}
    return render(request,'actors/maintenanceagent.html',context)



@allowed_users(allowed_roles=['admin'])
def viewStats(request):
    rooms = Room.objects.all()
    vehicles = Vehicle.objects.all()

    context={'rooms':rooms,'vehicles':vehicles, 'rooms':rooms}
    return render(request,'functions/stats.html',context)

@allowed_users(allowed_roles=['admin'])
def emergencies(request):

    rooms = Room.objects.all()
    obstacles = Obstacle.objects.all()
    incidents = Incident.objects.all()
    context={'rooms':rooms,'obstacles':obstacles,'incidents':incidents, 'rooms':rooms}
    return render(request,'functions/emergs.html',context)

def viewObstacles(request,pk):
    rooms = Room.objects.all()
    obstacle = Obstacle.objects.get(pk=pk)
    form = ObstaclesForm()
    if request.method =='POST':

        form = ObstaclesForm(request.POST,instance=obstacle)

        if form.is_valid():
            form.save()
            return redirect('emergencies')
        else:
            print(form.errors)

    context={'rooms':rooms,'obstacle':obstacle, 'form':form}

    return render(request,'functions/view-obstacles.html',context)

def viewIncidents(request,pk):
    rooms = Room.objects.all()
    incident = Incident.objects.get(pk=pk)
    form = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST , instance=incident)
        if form.is_valid():
            form.save()
            return redirect('emergencies')
        else:
            print(form.errors)

    context={'rooms':rooms,'incident':incident}

    return render(request,'functions/view-incidents.html',context)

@allowed_users(allowed_roles=['traincontrollers'])
def trainSchedual(request):
    rooms = Room.objects.all()
    schedules = Schedule.objects.all()
    context={'rooms':rooms,
        'schedules':schedules
    }
    return render(request,'functions/trainsched.html',context)

@allowed_users(allowed_roles=['traincontrollers'])
def createSchedual(request):
    rooms = Room.objects.all()
    vehicles = Vehicle.objects.all()
    form = ScheduleForm()
    username =request.user.username
    if request.method =='POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('train-schedual')
        else:
            print(form.errors)
    context={'rooms':rooms,'form':form,'username': username ,'vehicles':vehicles}
    return render(request,'functions/trainsched_create.html',context)

def editSchedual(request,pk):
    rooms = Room.objects.all()
    schedule=Schedule.objects.get(pk=pk)
    context={'rooms':rooms,'schedule':schedule}
    return render(request,'functions/trainsched-edit.html',context)

def updateSchedual(request,pk):
    rooms = Room.objects.all()
    schedule = Schedule.objects.get(pk=pk)
    form = ScheduleForm()
    if request.method =='POST':
        print("🙌")
        form = ScheduleForm(request.POST,instance=schedule)
        if form.is_valid():
            form.save()
            print("🙉")
            return redirect('train-schedual')
    context={'rooms':rooms,'schedule':schedule}
    return render(request,'functions/trainsched-edit.html',context)

def deleteSchedual(request,pk):
    rooms = Room.objects.all()
    schedule= Schedule.objects.get(pk=pk)
    schedule.delete()
    return redirect('train-schedual')

@allowed_users(allowed_roles=['traincontrollers'])
def incidents(request):
    rooms = Room.objects.all()
    incidents=Incident.objects.all()
    context={'rooms':rooms,'incidents':incidents}
    return render(request,'functions/incidents.html',context)

def createIncidents(request):
    recipient = request.user
    notification = Notification(recipient=recipient, message="Incident added")
    notification.save()
    rooms = Room.objects.all()
    vehicles = Vehicle.objects.all()
    form = ObstaclesForm()
    username =request.user.username
    if request.method =='POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incidents')
        else:
            print(form.errors)
    context={'rooms':rooms,'form':form,'username': username ,'vehicles':vehicles,'room':room}
    return render(request,'functions/incidents_create.html',context)

def editIncidents(request,pk):
    rooms = Room.objects.all()

    incident = Incident.objects.get(pk=pk)
    vehicles = Vehicle.objects.all()

    context={'rooms':rooms,'incident':incident,'vehicles':vehicles}
    return render(request,'functions/incidents_edit.html',context)

def updateIncidents(request,pk):
    rooms = Room.objects.all()
    incident = Incident.objects.get(pk=pk)
    vehicles = Vehicle.objects.all()
    form = IncidentForm()
    if request.method =='POST':

        form = IncidentForm(request.POST,instance=incident)
        if form.is_valid():
            form.save()
 
            return redirect('incidents')
    context={'rooms':rooms,'incident':incident,'vehicles':vehicles}
    return render(request,'functions/incidents_edit.html',context)

def deleteIncidents(request,pk):
    rooms = Room.objects.all()
    incident=Incident.objects.get(pk=pk)
    incident.delete()
    return redirect('incidents')



@allowed_users(allowed_roles=['fieldagents'])
def obstacles(request):

    rooms = Room.objects.all()
    obstacles = Obstacle.objects.all()
    
    context={'rooms':rooms,'obstacles':obstacles}
    return render(request,'functions/obstacles.html',context)

def createObstacles(request):
    recipient = request.user
    notification = Notification(recipient=recipient, message="Obstacle added")
    notification.save()
    rooms = Room.objects.all()
    form = ObstaclesForm()
    username =request.user.username
    if request.method =='POST':
        form = ObstaclesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('obstacles')
        else:
            print(form.errors)
    context={'rooms':rooms,'form':form,'username': username }
    return render(request,'functions/obstacles_create.html',context)

def editObstacle(request,pk):
    rooms = Room.objects.all()
    obstacle = Obstacle.objects.get(pk=pk)
    context = {'rooms':rooms,'obstacle':obstacle}
    return render(request,'functions/obstacles_edit.html',context)

def updateObstacle(request,pk):
    rooms = Room.objects.all()
    obstacle = Obstacle.objects.get(pk=pk)
    form = ObstaclesForm()
    if request.method =='POST':
        form = ObstaclesForm(request.POST,instance=obstacle)
        if form.is_valid():
            form.save()
            return redirect('obstacles')
    context={'rooms':rooms,'obstacle':obstacle}
    return render(request,'functions/obstacles_edit.html',context)

def deleteObstacle(request,pk):
    rooms = Room.objects.all()
    obstacle=Obstacle.objects.get(pk=pk)
    obstacle.delete()
    return redirect('obstacles')



@allowed_users(allowed_roles=['depotmanager'])
def maintenanceTeam(request):
    teams= TeamAssignment.objects.all()
    rooms = Room.objects.all()
    context={'rooms':rooms,'teams':teams}
    return render(request,'functions/maintenanceteam.html',context)


def createTeam(request):
    users = request.user
    rooms = Room.objects.all()
    form = TeamAssignmentForm()
    if request.method == 'POST':
        form = TeamAssignmentForm(request.POST)
        if form.is_valid():
            team = form.save()
 # Save the many-to-many relationship
            return redirect('maintenance-team')
        else:
            print(form.errors)
            
    context={'rooms':rooms,'form':form,'users':users}
    return render(request,'functions/team-create.html',context)





def editTeam(request,pk):
    rooms = Room.objects.all()
    team = Team.objects.get(pk=pk)
    context = {'rooms':rooms,'team':team}
    return render(request,'functions/team-edit.html',context)


def updateTeam(request,pk):
    rooms = Room.objects.all()
    team = Team.objects.get(pk=pk)
    form = TeamForm()
    if request.method =='POST':
        form = TeamForm(request.POST,instance=team)
        if form.is_valid():
            form.save()
            return redirect('maintenance-team')
    context={'rooms':rooms,'team':team}
    return render(request,'functions/team_edit.html',context)


def deleteTeam(request,pk):
    rooms = Room.objects.all()
    team=Team.objects.get(pk=pk)
    team.delete()
    return redirect('maintenance-team')



@allowed_users(allowed_roles=['depotmanager','maintenanceagents'])
def maintenanceSchedual(request):
    recipient = request.user
    notification = Notification(recipient=recipient, message="Schedule added")
    notification.save()
    rooms = Room.objects.all()
    maintenances = Maintenance.objects.all()
    context={'rooms':rooms,'maintenances':maintenances}
    return render(request,'functions/maintenancesched.html',context)

@allowed_users(allowed_roles=['depotmanager'])
def createMaintenance(request):
    rooms = Room.objects.all()
    vehicles=Vehicle.objects.all()    
    form = MaintenanceForm()
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
              # Save the many-to-many relationship
            return redirect('maintenance-schedual')
        else:
            print(form.errors)
            
    context={'rooms':rooms,'form':form,'vehicles':vehicles}
    return render(request,'functions/maintenance-create.html',context)

@allowed_users(allowed_roles=['depotmanager'])
def editMaintenance(request,pk):
    rooms = Room.objects.all()
    vehicles=Vehicle.objects.all()

    maintenance = Maintenance.objects.get(pk=pk)
    context = {'rooms':rooms,'maintenance':maintenance,'vehicles':vehicles}
    return render(request,'functions/maintenance-edit.html',context)

@allowed_users(allowed_roles=['depotmanager'])
def updateMaintenance(request,pk):
    rooms = Room.objects.all()
    vehicles=Vehicle.objects.all()
    maintenance = Maintenance.objects.get(pk=pk)
    form = MaintenanceForm()
    if request.method =='POST':
        form = MaintenanceForm(request.POST,instance=maintenance)
        if form.is_valid():
            form.save()
            return redirect('maintenance-schedual')
    context={'rooms':rooms,'maintenance':maintenance,'vehicles':vehicles}
    return render(request,'functions/maintenance-edit.html',context)

@allowed_users(allowed_roles=['depotmanager'])
def deleteMaintenance(request,pk):
    rooms = Room.objects.all()
    maintenance=Maintenance.objects.get(pk=pk)
    maintenance.delete()
    return redirect('maintenance-schedual')


@allowed_users(allowed_roles=['maintenanceagents'])
def vehicleStatus(request):
    rooms = Room.objects.all()
    vehicles=Vehicle.objects.all()
    statuss=StatusV.objects.all()
    context={'rooms':rooms,'statuss':statuss,'vehicles':vehicles}
    return render(request,'functions/status.html',context)

def createStatus(request):
    rooms = Room.objects.all()
    vehicles = Vehicle.objects.all()
    form = StatusForm()
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
              # Save the many-to-many relationship
            return redirect('vehicle-status')
        else:
            print(form.errors)
            
    context={'rooms':rooms,'form':form,'vehicles':vehicles}
    return render(request,'functions/status-create.html',context)


def editStatus(request,pk):
    rooms = Room.objects.all()
    vehicles = Vehicle.objects.all()
    status = StatusV.objects.get(pk=pk)
    context = {'rooms':rooms,'status':status,'vehicles':vehicles}
    return render(request,'functions/status-edit.html',context)


def updateStatus(request,pk):
    rooms = Room.objects.all()
    vehicles = Vehicle.objects.all()
    status = StatusV.objects.get(pk=pk)
    form = StatusForm()
    if request.method =='POST':
        form = StatusForm(request.POST,instance=status)
        if form.is_valid():
            form.save()
            return redirect('vehicle-status')
    context={'rooms':rooms,'form':form,'status':status,'vehicles':vehicles}
    return render(request,'functions/status-edit.html',context)


def deleteStatus(request,pk):
    rooms = Room.objects.all()
    status=StatusV.objects.get(pk=pk)
    status.delete()
    return redirect('vehicle-status')



@login_required(login_url='login')
@allowed_users(allowed_roles=['depotmanager','fieldagents','maintenanceagents','traincontrollers','admin'])
def profile(request):
    rooms = Room.objects.all() 
    context={'rooms':rooms}

    return render(request,'profile.html',context)

#  *************************************************************
def createRoom(request):
    recipient = request.user
    notification = Notification(recipient=recipient, message="Room added")
    notification.save()
    rooms = Room.objects.all()

    context = {'rooms':rooms,'notification':notification}
    if request.method == 'POST':
        room_name = request.POST['room_name']
        # Perform any additional validations or checks here
        if Room.objects.filter(name=room_name).exists():
            # Room already exists, handle the error or show a message
            return redirect('home')  # Redirect to the home page or any other desired page
        else:
            new_room = Room.objects.create(name=room_name)
            new_room.save()
            return redirect('/room/' + room_name + '/')
       
    else:
        return render(request, 'functions/create-room.html')
    

def room(request, room):

    rooms= Room.objects.all()
    username = request.user.username
    room_details = Room.objects.get(name=room)
    return render(request, 'functions/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'rooms':rooms,
        
    })


def send(request):

    message = request.POST['message']
    username = request.user.username
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
    # *************************************************************

def view_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(recipient=user).order_by('-timestamp')
    return render(request, 'parts/navbar.html', {'notifications': notifications})

