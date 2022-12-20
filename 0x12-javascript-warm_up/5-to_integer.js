#!/usr/bin/node
const firstArgument = process.argv[2];

const isNumber = !isNaN(firstArgument);

if (isNumber) {
  console.log(`My number: ${parseInt(firstArgument, 10)}`);
} else {
  console.log("Not a number");
}
