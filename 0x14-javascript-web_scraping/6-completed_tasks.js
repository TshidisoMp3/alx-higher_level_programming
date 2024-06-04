#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
    if (error) {
        console.error('error:', error);
    } else {
        const tasks = JSON.parse(body);
        const completedTasks = tasks.filter(task => task.completed === true);
        console.log(completedTasks.length);
    }
});
