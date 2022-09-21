$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const idx in data.results) {
    $('#list_movies').append('<li>' + data.results[idx].title + '</li>');
  }
});
