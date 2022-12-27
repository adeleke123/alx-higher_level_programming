#!/usr/bin/node
const fs = require('fs');
const [source1, source2, destination] = process.argv.slice(2);
const data1 = fs.readFileSync(source1, 'utf8');
const data2 = fs.readFileSync(source2, 'utf8');
const data = data1 + data2;
fs.writeFileSync(destination, data);
