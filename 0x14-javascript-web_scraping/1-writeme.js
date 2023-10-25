#!/usr/bin/node

const fs = require('fs');


if  (process.argv.length !== 4) {
    console.log("Usage: ./1-writeme.js <file_path> <string_to_write>");
} else {
    const filePath = process.argv[2];
    const content = process.argv[3];
    
    fs.writeFile(filePath, content, 'utf-8', (err) => {
        if (err) {
            console.log(err);
        }
    });
}