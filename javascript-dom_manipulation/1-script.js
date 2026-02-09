const redHeaderTrigger = document.querySelector('#red_header');
redHeaderTrigger.addEventListener('click', function() {
  const headerElement = document.querySelector('header');
  headerElement.style.color = '#FF0000';
});
