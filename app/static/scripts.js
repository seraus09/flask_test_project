function checkRecaptcha() {
    var response = grecaptcha.getResponse();
    if(response.length == 0) {
      //reCaptcha not verified
      alert('No pass');
    }
    else {
      //reCaptch verified
      fetch(`/getdata/${response}`, {method: 'POST'})
          .then(function (response) {
              return response.text();
          });
    } 
  }
    document.getElementById('ping').onclick = function() {
      checkRecaptcha();
    };