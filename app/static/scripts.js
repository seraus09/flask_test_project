function checkRecaptcha() {
    var response = grecaptcha.getResponse();
    if(response.length == 0) {
      //reCaptcha not verified
      alert('No pass');
    }
    else {
      //reCaptch verified
      let status = 'Ok';
      fetch(`/getdata/${status}`, {method: 'POST'})
          .then(function (response) {
              return response.text();
          });
    } 
  }
    document.getElementById('ping').onclick = function() {
      checkRecaptcha();
    };