document.addEventListener("DOMContentLoaded", function() {

  const heading = document.getElementById('attractive-heading');
  const texts = ["Welcome to SmartYatra!", "Plan your journey here!"];
  let textIndex = 0;
  let charIndex = 0;

  function displayText() {
    if (charIndex < texts[textIndex].length) {
      heading.textContent += texts[textIndex].charAt(charIndex);
      charIndex++;
      setTimeout(displayText, 100);
    } else {
      charIndex = 0;
      textIndex = (textIndex + 1) % texts.length;
      setTimeout(() => {
        heading.textContent = '';
        displayText(); 
      }, 1000);
    }
  }
  displayText();

var L1 = [25.45017, 82.85399];
var L2 = [25.49412, 82.82037];
var L3= [25.49412, 83.82037];

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

L.marker(L3).addTo(map)
.bindPopup('L3')
.openPopup();

L.Routing.control({
  waypoints: [
    L.latLng(25.45017, 82.85399),
    L.latLng(25.49412, 83.82037)
  ]
}).addTo(map);

});