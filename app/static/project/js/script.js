let menuIcon = document.querySelector('.menu')
let navItems = document.querySelector('.nav-items')

menuIcon.addEventListener('click', () => {
  menuIcon.classList.toggle('ri-menu-line')
  menuIcon.classList.toggle('ri-close-line')
  navItems.classList.toggle('right-0')
})

function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    obj.innerHTML = Math.floor(progress * (end - start) + start);
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}

const obj1 = document.querySelector('#value1')
animateValue(obj1, 0, 100, 2000);

const obj2 = document.querySelector('#value2')
animateValue(obj2, 0, 5000, 3000);

const obj3 = document.querySelector('#value3')
animateValue(obj3, 0, 17, 1000);

var swiper = new Swiper(".mySwiper", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});