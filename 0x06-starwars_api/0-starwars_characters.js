const request = require('request');

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, function (error,
response, body) {
    if (!error && response.statusCode === 200) {
        const characters = JSON.parse(bady).characters;
        characters.forEach((characterUrl) => {
          request(characterUrl, function (error, response, body) {
            if (!error && request.statusCode === 200) {
                const characterName = JSON.parse(body).name;
                console.log(characterName);
            }
          });
        });
    }
});

