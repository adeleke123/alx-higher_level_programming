#!/usr/bin/node
const args = process.argv.slice(2);  /* Get the arguments passed to the script, excluding the first two elements (which are the path to Node.js and the path to the script) */
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
