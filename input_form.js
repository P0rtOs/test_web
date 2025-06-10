const phoneInput = document.querySelector('#phone');
if (phoneInput) {
  intlTelInput(phoneInput, {
    initialCountry: 'br',
    utilsScript: 'https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js'
  });
}

document.querySelector('#contact-form').addEventListener('submit', function(e) {
  e.preventDefault();
  if (!this.checkValidity()) {
    this.reportValidity();
    return;
  }
  window.location.href = 'thankyou.html';
});

document.querySelectorAll('a[href="#form-section"]').forEach(function(link){
  link.addEventListener('click', function(e){
    e.preventDefault();
    document.querySelector('#form-section').scrollIntoView({behavior: 'smooth'});
  });
});
