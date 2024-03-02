document.addEventListener("DOMContentLoaded", function () {
    var map = L.map('map').setView([25.3356, 82.9221], 11);
  
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

});   