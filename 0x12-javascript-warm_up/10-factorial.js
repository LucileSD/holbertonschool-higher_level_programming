#!/usr/bin/node
/**
 * computes and prints a factorial
 */
function factorial (a) {
  if (a === 1 || !a) return (1);
  else return (a * factorial(a - 1));
}
console.log(factorial(Number(process.argv[2])));
