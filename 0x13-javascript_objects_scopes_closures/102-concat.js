#!/usr/bin/node
const fs = require('fs');
const [src1, src2, dest] = process.argv.slice(2);
const data1 = fs.readFileSync(src1, 'utf8');
const data2 = fs.readFileSync(src2, 'utf8');
fs.writeFileSync(dest, `${data1}\n${data2}`);
