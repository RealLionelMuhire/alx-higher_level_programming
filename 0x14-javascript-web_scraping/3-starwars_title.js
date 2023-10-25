#!/usr/bin/node

const { error } = require('console');
const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: node 3-starwars_title.js <movie_id>');
    process.exit(1);
}

const movie_id = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error('Error:', response.statusCode);
        process.exit(1);
    }

    const movie_data = JSON.parse(body);
    console.log(movie_data.title);
});