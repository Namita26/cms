var SERVER_URL = "http://localhost:5000";
var BASE_URL = "http://localhost";

function validate_token(id_token){
	$.ajax({
	      url: SERVER_URL + "/auth",
	      type: 'GET',
	      data: {"id_token": id_token},
	      success: function(data){
	      	  // TODO : store the token in the cookie using jquery cookie
	          window.location.href = BASE_URL + "/templates/concept_creation.html"
	      },
	      error: function(data){
	      	  // TODO : Get the message from the server.
	      	  window.location.href = BASE_URL + "?error=Error in Authentication"
	      }
	  });
}
