#!/usr/bin/node
function factorial (nbr) {
  if (!nbr || nbr < 2) {
    return (1);
  }
  return nbr * factorial(nbr - 1);
}
console.log(factorial(Number(process.argv[2])));
