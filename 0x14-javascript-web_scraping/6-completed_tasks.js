#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
    console.error('Usage: ./6-completed_tasks.js <API_URL>');
    process.exit(1);
}


const api_url = process.argv[2];

request(api_url, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error('Error:'. response.statusCode);
        process.exit(1);
    }

    try {
        const data = JSON.parse(body);

        const completed_tasks = {}

        data.forEach((task) => {
            const userId = task.userId;
            if (task.completed) {
                if (completed_tasks[userId]) {
                    completed_tasks[userId]++;
                } else {
                    completed_tasks[userId] = 1;
                }
            }
        });

        console.log(completed_tasks);
    } catch (parseError) {
        console.error('Error parsing JSON:', parseError);
        process.exit(1);
    }
});
