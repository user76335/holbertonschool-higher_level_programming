const redHeaderTrigger = document.querySelector('#red_header');
redHeaderTrigger.addEventListener('click', function() {
  const headerElement = document.querySelector('header');
    headerElement.classList.add('red');
});
