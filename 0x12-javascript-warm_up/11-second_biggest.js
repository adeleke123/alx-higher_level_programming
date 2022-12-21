#!/usr/bin/node
function findSecondLargest() {
  if (arguments.length < 2) {
    console.log(0);
    return;
  }

  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;
  for (const arg of arguments) {
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
