#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    function fetchCharacterName(index) {
      if (index < characterUrls.length) {
        request(characterUrls[index], (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error(characterError);
          } else if (characterResponse.statusCode !== 200) {
            console.error(`Character request failed with status code ${characterResponse.statusCode}`);
          } else {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
            fetchCharacterName(index + 1);
          }
        });
      }
    }

    fetchCharacterName(0);
  }
});