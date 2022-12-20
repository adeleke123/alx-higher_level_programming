#!/usr/bin/node
let argument = process.argv[2];

if (argument === undefined) {
  console.log("No argument");
} else {
  console.log(argument);
}
