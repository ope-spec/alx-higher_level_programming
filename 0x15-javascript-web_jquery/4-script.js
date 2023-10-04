$(document).ready(function() {
	var toggleHeaderDiv = $('#toggle_header');
  
	toggleHeaderDiv.click(function() {
	  $('header').toggleClass('red green');
	});
});
