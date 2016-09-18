$(document).ready(function(){
	// Add in the value for the input element so that the user
  // can tweak the incorrect email address entered.
  var email = $('#entered_email').attr('email');
  $('input#email').attr('value', email)
});
