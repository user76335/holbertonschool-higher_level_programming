const toggleTrigger = document.querySelector('#toggle_header');
toggleTrigger.addEventListener('click', function() {
  const headerElement = document.querySelector('header');
   if (headerElement.classList.contains('red')) {
    headerElement.classList.remove('red');
    headerElement.classList.add('green');
  } else {
    headerElement.classList.remove('green');
    headerElement.classList.add('red');
  }
});
