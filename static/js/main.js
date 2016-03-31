var SERVER_URL = "http://localhost:5000";
var BASE_URL = "http://localhost";

function validate_token(id_token){
	console.log("In validate token");
	$.ajax({
	      url: SERVER_URL + "/auth",
	      type: 'GET',
	      data: {"id_token": id_token},
	      success: function(data){
	      	  // TODO : store the token in the cookie using jquery cookie
	      	  console.log("In succes of idtoken-------------------")
	      	  console.log(data)
	          window.location.href = BASE_URL + "/templates/dashboard.html";
	      },
	      error: function(data){
	      	  // TODO : Get the message from the server.
	      	  console.log(data);
	      	  window.location.href = BASE_URL + "/templates/unauthorised.html";
	      }
	  });
}
