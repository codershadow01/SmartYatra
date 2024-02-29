document.addEventListener("DOMContentLoaded", function() {
var L1 = [25.45017, 82.85399];
var L2 = [25.49412, 82.82037];

// Initialize the map
var map = L.map('map').setView([25.3356, 82.9221], 11);

// Add a tile layer (map background)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker(L1).addTo(map)
.bindPopup('L1')
.openPopup();

L.marker(L2).addTo(map)
.bindPopup('L2')
.openPopup();

var path = L.polyline([
L1,
L2,
], { color: 'blue' }).addTo(map);
});