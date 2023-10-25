#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const { error } = require('console');

if (process.argv.length !== 4) {
    console.error('Usage: ./5-request_store.js <URL> <file_path>');
    process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.log('Error:', response.statusCode);
        process.exit(1);
    }

    fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            process.exit(1);
        }
    });
});