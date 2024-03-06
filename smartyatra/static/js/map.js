document.addEventListener("DOMContentLoaded", function () {
  var map = L.map('map').setView([25.373974072079754, 83.05496697777791], 12);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  const routes_list = JSON.parse(document.getElementById('routes_list').value);

  if (routes_list.length >= 1) {

    var waynames = [];
    var waypoints = [];
    for (let i = 0; i < routes_list.length; i++) {
      waynames.push(routes_list[i].node1.node_name);
      waypoints.push(L.latLng(routes_list[i].node1.lat, routes_list[i].node1.lon));
      if (i == routes_list.length - 1) {
        waynames.push(routes_list[i].node2.node_name);
        waypoints.push(L.latLng(routes_list[i].node2.lat, routes_list[i].node2.lon));
      }
    }

    L.Routing.control({
      waypoints: waypoints,
    }).addTo(map);

    waypoints.forEach(function (waypoint, index) {
      var marker = L.marker(waypoint).addTo(map);
      marker.bindPopup(waynames[index]).openPopup();
    });
  }

});