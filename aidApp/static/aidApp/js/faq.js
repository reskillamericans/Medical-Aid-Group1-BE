var acc = document.getElementsByClassName("accordion");

var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var panel = this.nextElementSibling;
      if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
      } else {
        let active = document.querySelectorAll(".accordion-div .accordion.active");
        for(let j = 0; j < active.length; j++){
          active[j].classList.remove("active");
          active[j].nextElementSibling.style.maxHeight = null;
        }
        this.classList.toggle("active");
      panel.style.maxHeight = panel.scrollHeight + "px";
      }
      
    });
  }

  /* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function myFunction() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
