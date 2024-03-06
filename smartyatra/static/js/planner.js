document.addEventListener("DOMContentLoaded", function() {
   
  const heading = document.getElementById('attractive-heading');
  const texts = ["Find Public Transport!"];
  let textIndex = 0;
  let charIndex = 0;

  function displayText() {
    if (charIndex < texts[textIndex].length) {
      heading.textContent += texts[textIndex].charAt(charIndex);
      charIndex++;
      setTimeout(displayText, 100);
    } else {
      charIndex = 0;
      textIndex++;
    }
  }
  displayText();

  window.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('route-form');
    form.addEventListener('submit', function (event) {
      var sourceInput = document.getElementById("source");
      var destinationInput = document.getElementById("destination");

      if (sourceInput.value.trim() === "" || destinationInput.value.trim() === "") {
        var myModal = new bootstrap.Modal(document.getElementById('validationModal'), {
          keyboard: false
        });
        myModal.show();
        event.preventDefault();
      }

    });
  });
});