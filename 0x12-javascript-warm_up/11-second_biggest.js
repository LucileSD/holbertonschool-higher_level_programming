#!/usr/bin/node
/**
 *  searches the second biggest integer in the list of arguments
 */
const array = [];
let i;
if (process.argv.length <= 3) console.log(0);
else {
  for (i = 2; i < process.argv.length; i++) {
    if (!isNaN(process.argv[i])) array.push(process.argv[i]);
  }
  array.sort(function (a, b) { return a - b; });
  const size = array.length;
  console.log(array[size - 2]);
}
