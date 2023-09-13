#!/usr/bin/node
const name = process.argv[2];
if (!name) { console.log('No argument'); } else {
  console.log(name);
}
