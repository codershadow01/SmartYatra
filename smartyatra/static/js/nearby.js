document.addEventListener("DOMContentLoaded", function() {
   
    const heading = document.getElementById('attractive-heading');
    const texts = ["Welcome to SmartYatra!", "Find your nearest stops!"];
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
  });