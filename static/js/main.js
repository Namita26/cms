var SERVER_URL = "http://cms.glamrs.com:5000";
var BASE_URL = "http://cms.glamrs.com";
var ROLE = "";

function validate_token(id_token){
	console.log("In validate token");
	$.ajax({
	      url: SERVER_URL + "/auth",
	      type: 'GET',
	      data: {"id_token": id_token},
	      success: function(data){
	      	  data = JSON.parse(data);
	      	  ROLE = data.role;
	      	  useremail = data.email;
	          window.location.href = BASE_URL + "/templates/dashboard.html?role="+ROLE+"&email="+useremail;
	      },
	      error: function(data){
	      	  window.location.href = BASE_URL + "/templates/unauthorised.html";
	      }
	  });
}

  function signOut() {
  	
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
  }


