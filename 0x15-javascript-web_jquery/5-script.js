$(document).ready(function() {
	var addItemDiv = $('#add_item');
  
	addItemDiv.click(function() {
	  var newItem = $('<li>').text('Item');
  
	  $('ul.my_list').append(newItem);
	});
});
