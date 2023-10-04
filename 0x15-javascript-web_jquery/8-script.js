$(document).ready(function() {
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
	  var movies = data.results;
  
	  var listMovies = $('#list_movies');
  
	  $.each(movies, function(index, movie) {
		var title = movie.title;
		var listItem = $('<li>').text(title);
		listMovies.append(listItem);
	  });
	});
});
