#!/usr/bin/node
/**
 * prints a square
 */
const size = process.argv[2];
let line;
const sign = 'X';
if (!size || isNaN(process.argv[2])) console.log('Missing size');
else {
  for (line = 0; line < size; line++) {
    console.log(sign.repeat(size));
  }
}
