$(document).ready(function() {
	function fetchTranslation() {
	  var languageCode = $('#language_code').val();
  
	  var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;
  
	  $.get(apiUrl, function(data) {
		$('#hello').text(data.hello);
	  });
	}
  
	$('#btn_translate').click(function() {
	  fetchTranslation();
	});
  
	$('#language_code').keypress(function(event) {
	  if (event.keyCode === 13) {
		fetchTranslation();
	  }
	});
});
