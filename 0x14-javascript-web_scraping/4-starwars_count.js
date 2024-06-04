#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.error('error:', error);
    } else {
        let count = 0;
        const films = JSON.parse(body).results;
        for (const film of films) {
            for (const character of film.characters) {
                if (character.includes('18')) {
                    count++;
                }
            }
        }
        console.log(count);
    }
});
