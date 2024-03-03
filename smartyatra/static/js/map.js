document.addEventListener("DOMContentLoaded", function () {
  var map = L.map('map').setView([25.3356, 82.9221], 11);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  var routesDataElements = document.getElementById('routes-data'); 

  function extractData(dataString) {
    var routess = dataString.slice(2, -2).split("), (");
    var routesDataValues = [];
    routess.forEach(function (routesString) {
      var routesValues = routesString.replace(/[\(\)]/g, '').split(", ");
      var routes = routesValues.map(function (value) {
        return isNaN(value) ? value : parseFloat(value);
      });
      routesDataValues.push(routes);
    });
    return routesDataValues;
  }
  
 
  var routesDataValues = extractData(routesDataElements.value);
  var waynames=[];

  if (routesDataValues.length > 0) {
    var lastIndex = routesDataValues.length - 1;
    var waypoints = [];
    routesDataValues.forEach(function (route,index) {
          waypoints.push(L.latLng(route[2], route[3]));
          var cleanedRouteName = route[1].replace(/^\\u0027|\\u0027$/g, '');
          waynames.push(cleanedRouteName);

          if(index == lastIndex){
            waypoints.push(L.latLng(route[5], route[6]));
            var cleanedRouteName = route[4].replace(/^\\u0027|\\u0027$/g, '');
            waynames.push(cleanedRouteName);
          }
    });

    L.Routing.control({
      waypoints: waypoints,
  }).addTo(map);

  waypoints.forEach(function (waypoint,index) {
     var marker=L.marker(waypoint).addTo(map);
      marker.bindPopup(waynames[index]).openPopup();
  });
}
});