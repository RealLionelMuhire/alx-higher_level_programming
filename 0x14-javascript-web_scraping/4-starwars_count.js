#!/usr/bin/node


const request = require('request');


if (process.argv.length !== 3) {
    console.error('Usage: ./4-starwars_count.js <api_url>');
    exit(1)
}

const api_url = process.argv[2];

request(api_url, (error, response, body) => {
    if (error){
        console.error('Error:', error);
        process.exit(1);
    }

    const movieData = JSON.parse(body);

    const wedgeMovies = movieData.results.filter((movie) =>
    movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));

    console.log(wedgeMovies.length);
});