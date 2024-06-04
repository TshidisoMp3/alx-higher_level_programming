#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.error('error:', error);
    } else {
        fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
            if (err) {
                console.log(err);
            }
        });
    }
});
