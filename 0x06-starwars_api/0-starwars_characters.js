#!/usr/bin/node
// script that prints all characters of a Star Wars movie:
const request = require('request');

const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}/`,
function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        }
      });
    });
  }
});
