#!/usr/bin/node
/**
 *  prints x times “C is fun”
 */
const x = process.argv[2];
let i;
if (!x) console.log('Missing number of occurrences');
else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
