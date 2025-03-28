from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutPage, name='logout'),
    path('',views.home, name='home'),
    path('vehicle-positions/', views.vehicle_positions, name='vehicle-positions/'),
    path('station-positions/', views.station_positions, name='station-positions/'),
    path('redX/', views.redX, name='redX/'),
    path('redX2/', views.redX2, name='redX2/'),
    

    path('op-manager/', views.opManager, name='op-manager'),
    path('train-controller/', views.trainController, name='train-controller'),
    path('field-agent/', views.fieldAgent, name='field-agent'),
    path('depot-manager/', views.depotManager, name='depot-manager'),
    path('maitenance-agent/', views.maitenanceAgent, name='maitenance-agent'),
    path('stats/', views.viewStats, name='stats'),

    path('emergencies/', views.emergencies, name='emergencies'),
    path('view-obstacles/<str:pk>', views.viewObstacles, name='view-obstacles'),
    path('view-incidents/<str:pk>', views.viewIncidents, name='view-incidents'),

    path('train-schedual/', views.trainSchedual, name='train-schedual'),
    path('create-schedual/', views.createSchedual, name='create-schedual'),
    path('edit-schedual/<str:pk>', views.editSchedual, name='edit-schedual'),
    path('update-schedual/<str:pk>', views.updateSchedual, name='update-schedual'),
    path('delete-schedual/<str:pk>', views.deleteSchedual, name='delete-schedual'),

    path('incidents/', views.incidents, name='incidents'),
    path('create-incidents/', views.createIncidents, name='create-incidents'),
    path('edit-incidents/<str:pk>', views.editIncidents, name='edit-incidents'),
    path('update-incidents/<str:pk>', views.updateIncidents, name='update-incidents'),
    path('delete-incidents/<str:pk>', views.deleteIncidents, name='delete-incidents'),

    path('obstacles/', views.obstacles, name='obstacles'),
    path('create-obstacle/', views.createObstacles, name='create-obstacle'),
    path('edit-obstacle/<str:pk>', views.editObstacle, name='edit-obstacle'),
    path('update-obstacle/<str:pk>', views.updateObstacle, name='update-obstacle'),
    path('delete-obstacle/<str:pk>', views.deleteObstacle, name='delete-obstacle'),

    path('maintenance-team/', views.maintenanceTeam, name='maintenance-team'),
    path('create-team',views.createTeam,name='create-team'),
    path('edit-team/<str:pk>',views.editTeam,name='edit-team'),
    path('update-team/<str:pk>',views.updateTeam,name='update-team'),
    path('delete-team/<str:pk>',views.deleteTeam,name='delete-team'),

    path('maintenance-schedual/', views.maintenanceSchedual, name='maintenance-schedual'),
    path('create-maintenance/', views.createMaintenance, name='create-maintenance'),
    path('edit-maintenance/<str:pk>', views.editMaintenance, name='edit-maintenance'),
    path('update-maintenance/<str:pk>', views.updateMaintenance, name='update-maintenance'),
    path('delete-maintenance/<str:pk>', views.deleteMaintenance, name='delete-maintenance'),

    path('vehicle-status/', views.vehicleStatus, name='vehicle-status'),
    path('create-status/', views.createStatus, name='create-status'),
    path('edit-status/<str:pk>', views.editStatus, name='edit-status'),
    path('update-status/<str:pk>', views.updateStatus, name='update-status'),
    path('delete-status/<str:pk>', views.deleteStatus, name='delete-status'),

    path('profile/', views.profile, name='profile'),
# **********************************************
    path('create-room/', views.createRoom, name='create-room'),
    path('room/<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
    # *********************************************

]