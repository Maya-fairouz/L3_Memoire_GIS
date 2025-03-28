

function createMap(center , zoom){
    let map =L.map('map').setView(center,zoom);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);
    return map
    
}

function updateMarkers(markerFeatureGroup){
    // send a request ro the server to get the new lat and long data
    
    // http request to the backend
    fetch('/vehicle-positions/').then(response => response.json()).then(data => {
      // markerFeatureGroup;
      markerFeatureGroup.clearLayers();
      data.vehicles.forEach(vehicle => {
        let newLatLon = [vehicle.latitude, vehicle.longitude]
        vehiclePopup= L.marker(newLatLon).addTo(markerFeatureGroup.bindPopup('Vehicle :'+vehicle.name+ ', Speed :'+vehicle.speed+' km/h'));

       

        // console.log(vehicle,' : AAA',newLatLon
      })

    })   // specify the end point  
}
function stationMarkers( stationFeatureGroup) {
  // Send a request to the server to get the station data
  fetch('/station-positions/').then(response => response.json()).then(data => {
    // Clear existing markers from the feature group 
    stationFeatureGroup.clearLayers();
    var stationIcon = L.icon({
      
      iconUrl: '/static/tramStop.png',
      iconSize:  [35, 35], // size of the icon
      className: 'aaaaaaa'
    }); 
    
    // Iterate through the station data and add markers
    data.stations.forEach(station => {
      let newLatLon = [station.lat_station, station.long_station];

      L.marker(newLatLon ,{icon: stationIcon}).addTo(stationFeatureGroup).bindPopup('Station : ' +station.name_station);

      
    });
  });
}

function alertMarkers(alertFeatureGroup){
  fetch('redX/').then(response=> response.json()).then(data => {

  // alertFeatureGroup.clearLayers(); 
  var alertIcon = L.icon({
      
    iconUrl: '/static/redX.png',
    iconSize:  [35, 35], // size of the icon
    className: 'aaaaaaa'
  });  
  data.obstacles.forEach(obstacle => {
  
  let newLatLon = obstacle.location.split(',').map(parseFloat);


  // let newLatLon = JSON.parse(obstacle.location);
  
    // let newLatLon =[obstacle.location]
    var fix = "Fixed"
   
    if (obstacle.status == fix){
      console.log("im smart 🫶"+ obstacle.description);
      // add here a code to remove marker 
    }
    else{
      L.marker(newLatLon,{icon: alertIcon}).addTo(alertFeatureGroup).bindPopup('obstacle : '+obstacle.description);
    }
  })
  })
}


function alertMarkers2(alertFeatureGroup){
  fetch('redX2/').then(response=> response.json()).then(data => {

  // alertFeatureGroup.clearLayers(); 
  var alertIcon = L.icon({
      
    iconUrl: '/static/redX.png',
    iconSize:  [35, 35], // size of the icon

  
  });  
  data.incidents.forEach(incident => {
  
  let newLatLon = incident.location.split(',').map(parseFloat);


  // let newLatLon = JSON.parse(obstacle.location);
  
    // let newLatLon =[obstacle.location]

    L.marker(newLatLon,{icon: alertIcon}).addTo(alertFeatureGroup).bindPopup('Incident : '+incident.description);
  
    // 😶‍🌫️ it checks if the status is fixed then it removes the marker 
  })
  })
}