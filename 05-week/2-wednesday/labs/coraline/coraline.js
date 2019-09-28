//Credit: https://en.wikipedia.org/wiki/Ajax_%28programming%29
// This is the client-side script.

// Initialize the HTTP request.
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://www.omdbapi.com/?i=tt0327597&apikey=e03ca193");

// Track the state changes of the request.
xhr.onreadystatechange = function() {
  var DONE = 4; // readyState 4 means the request is done.
  var OK = 200; // status 200 is a successful return.
  if (xhr.readyState === DONE) {
    if (xhr.status === OK) {
      console.log(xhr.responseText); // 'This is the output.'
      console.log(JSON.parse(xhr.responseText));
    } else {
      console.log("Error: " + xhr.status); // An error occurred during the request.
    }
  }
};
xhr.send(null);

// AJAX
$.ajax({
  type: "GET",
  url: "http://www.omdbapi.com/?i=tt0327597&apikey=e03ca193",
  dataType: "JSON", // data type expected from server
  success: function(response) {
    console.log(response);
    showMovieDetails(
        response.Title, response.Released, response.Genre, response.Rated, response.Plot
        );
  },
  error: function(error) {
    console.log("Error: " + error);
  }
});

function showMovieDetails(title, released, genre, rated, plot) {
  var heading = $("<h1/>").text(title);
  $("#header").append(heading);
  var released = $("<h2/>").text(released);
  $("#header").append(released);
  var genre = $("<h3/>").text(genre);
  $("#section-one").append(genre);
  var rated = $("<h4/>").text(rated);
  $("#section-one").append(rated);
  var plot = $("<p1/>").text(plot);
  $("#section-two").append(plot);
  

}
$("#image-button").click(function(e) {
  e.preventDefault();
  setTimeout(function(url) { window.location = "evil-mother.jpeg" }, 2000, this.href);
});