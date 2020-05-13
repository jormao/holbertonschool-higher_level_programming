#!/usr/bin/node
// script that prints the title of a Star Wars movie where
// the episode number matches a given integer.
// The first argument is the movie ID
// You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
// You must use the module request
const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/', function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
