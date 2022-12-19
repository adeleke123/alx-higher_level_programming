#!/usr/bin/node
const args = process.argv.slice(2);  /* Get the arguments passed to the script, excluding the first two elements (which are the path to Node.js and the path to the script) */

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
/*
 This script uses the process.argv array to get the arguments passed to the script. The process.argv array contains the command-line arguments passed to the Node.js process, with the first element being the path to Node.js and the second element being the path to the script. Therefore, we slice the array to exclude the first two elements and get only the arguments passed to the script.

Then, we use an if...else statement to check the length of the args array and print a different message depending on the number of arguments. If the length of the args array is 0, it means that no arguments were passed to the script, so we print "No argument". If the length of the args array is 1, it means that only one argument was passed to the script, so we print "Argument found". Otherwise, we print "Arguments found".

 */
