#!/usr/bin/node
// script that prints all characters of a Star Wars movie

const request = require('request');
if (process.argv.length === 3) {
  const movieID = process.argv[2];
  const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
  request(url, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      const characterList = JSON.parse(body).characters;
      for (let i = 0; i < characterList.length; i++) {
        console.log(characterList[i]);
      }
    }
  });
}
