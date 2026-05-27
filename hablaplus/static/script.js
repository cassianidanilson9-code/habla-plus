// formulario email
document.getElementById("form").addEventListener("submit", function(e){
  e.preventDefault();

  const name = this.name.value;
  const email = this.email.value;
  const msg = this.message.value;

  window.location.href =
  `mailto:cassianidanilson9@gmail.com?subject=Contacto ${name}&body=${msg} (${email})`;
});

// scroll reveal
const elements = document.querySelectorAll(".reveal");

window.addEventListener("scroll", () => {
  elements.forEach(el => {
    const top = el.getBoundingClientRect().top;
    if(top < window.innerHeight - 100){
      el.classList.add("active");
    }
  });
});