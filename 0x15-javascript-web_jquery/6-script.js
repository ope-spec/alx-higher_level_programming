$(document).ready(function() {
	var updateHeaderDiv = $('#update_header');
  
	updateHeaderDiv.click(function() {
	  $('header').text('New Header!!!');
	});
});
