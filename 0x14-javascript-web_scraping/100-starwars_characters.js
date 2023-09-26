#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchCharacterName(url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Character request failed with status code ${response.statusCode}`);
    } else {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    }
  });
}
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    characterUrls.forEach((url) => {
      fetchCharacterName(url);
    });
  }
});
