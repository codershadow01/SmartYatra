document.addEventListener("DOMContentLoaded", function() {
var location1 = [25.45017, 82.85399];
var location2 = [25.49412, 82.82037];

// Initialize the map
var map = L.map('map').setView([25.3356, 82.9221], 11);

// Add a tile layer (map background)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Add markers for the two locations
L.marker(location1).addTo(map)
  .bindPopup('Location 1')
  .openPopup();

L.marker(location2).addTo(map)
  .bindPopup('Location 2')
  .openPopup();

});