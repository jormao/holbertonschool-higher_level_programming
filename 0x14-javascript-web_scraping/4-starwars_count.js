#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.
// The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
// Wedge Antilles is character ID 18
// You must use the module request
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let count = 0;
    for (const movie of JSON.parse(body).results) {
      for (const i of movie.characters) {
        if (i.search('/18/') > 0) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
