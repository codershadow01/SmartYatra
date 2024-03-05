document.addEventListener("DOMContentLoaded", function () {
    var map = L.map('map').setView([25.3356, 82.9221], 11);
  
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var services = JSON.parse(document.getElementById('nearby-stops').value);

    if (services.length > 0) {
      waypoints = [];
      services.forEach(function (stops) {
        waypoints.push(L.latLng(stops.node.lat, stops.node.lon));
      });
      
      waypoints.forEach(function (waypoint,index) {
        var marker=L.marker(waypoint).addTo(map);
        marker.bindPopup(services[index].node.node_name).openPopup();
      });
    }
});   