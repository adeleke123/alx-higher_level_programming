#!/usr/bin/node
function findSecondLargest(args) {
  if (args.length <= 1) {
    console.log(0);
    return;
  }

  let largest = -Infinity;
  let secondLargest = -Infinity;
  for (const arg of args) {
    const num = Number(arg);
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest) {
      secondLargest = num;
    }
  }
  console.log(secondLargest);
}

findSecondLargest(process.argv.slice(2));
