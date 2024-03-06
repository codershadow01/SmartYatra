document.addEventListener("DOMContentLoaded", function () {
  var map = L.map('map').setView([25.3356, 82.9221], 11);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // function convert_time(totalMinutes) {
  //   const hours = Math.floor(totalMinutes / 60);
  //   const minutes = totalMinutes % 60;
  //   const roundedMinutes = minutes.toFixed(0);
  //   let timeString = '';
  //   if (hours > 0) {
  //     timeString += `${hours} hr `;
  //   }
  //   if (roundedMinutes > 0) {
  //     timeString += `${roundedMinutes} min`;
  //   }
  //   return timeString.trim();
  // }

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

  var currentTime = new Date();
  var hours = currentTime.getHours();
  var minutes = currentTime.getMinutes();
  var seconds = currentTime.getSeconds();

  // console.log(hours + ":" + minutes + ":" + seconds);

  // Get current date and time
  var currentTime = new Date();

  // Set options for Indian time zone
  var options = {
    timeZone: 'Asia/Kolkata',
    hour12: false, // Set to true if you want 12-hour format
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  };

  // Get current time in Indian time zone format
  var indianTime = currentTime.toLocaleTimeString('en-IN', options);

  // console.log("Current time in India: " + indianTime);


});