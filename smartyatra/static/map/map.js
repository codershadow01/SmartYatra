var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var source = L.marker([51.5, -0.09]).addTo(map);
source.bindPopup('Source').openPopup();

var destination = L.marker([51.51, -0.1]).addTo(map);
destination.bindPopup('Destination').openPopup();

var latlngs = [
    [51.5, -0.09],
    [51.51, -0.1]
];
var polyline = L.polyline(latlngs, {color: 'blue'}).addTo(map);

var bounds = L.latLngBounds([51.5, -0.09], [51.51, -0.1]);
map.fitBounds(bounds);
