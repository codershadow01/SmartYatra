document.addEventListener("DOMContentLoaded", function () {
    var map = L.map('map').setView([25.3356, 82.9221], 11);
  
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var stops=this.getElementById("nearby-stops");
    console.log(stops.value);

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
   
    var routesDataValues = extractData(stops.value);
    console.log(routesDataValues);

});   