const updateTrigger = document.querySelector('#update_header');
updateTrigger.addEventListener('click', function() {
  const headerElement = document.querySelector('header');  
  headerElement.textContent = 'New Header!!!';
});
