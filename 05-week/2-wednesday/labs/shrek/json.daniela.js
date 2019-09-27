// This is the client-side script.

// Initialize the HTTP request.
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://www.omdbapi.com/?i=tt0126029&apikey=e03ca193");

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
  url: "http://www.omdbapi.com/?i=tt0126029&apikey=e03ca193",
  dataType: "JSON", // data type expected from server
  success: function(response) {
    console.log(response);
    showMovieDetails(response.Title, response.Released, response.Plot, response.Rated);
  },
  error: function(error) {
    console.log("Error: " + error);
  }
});


function showMovieDetails(title, released, plot, rated) {
  var heading = $("<h1/>").text(title);
  $("#header").append(heading);
  var rated = $("<h2/>").text(rated);
  $("#header").append(rated);
  var released = $("<h3/>").text(released);
  $("#header").append(released);
  var plot = $("<p1/>").text(plot);
  $("body").append(plot);
}


