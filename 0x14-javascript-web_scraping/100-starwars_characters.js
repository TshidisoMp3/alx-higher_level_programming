#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.error('error:', error);
    } else {
        const films = JSON.parse(body).results;
        for (const film of films) {
            for (const character of film.characters) {
                if (character.includes('18')) {
                    console.log(film.title);
                    break;
                }
            }
        }
    }
});
