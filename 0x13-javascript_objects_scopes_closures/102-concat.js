#!/usr/bin/node
/**
 * concats 2 files
 */
const fs = require('fs');

const A = process.argv[2];
const B = process.argv[3];
const C = process.argv[4];

fs.readFile(A, 'utf8', (err, fileA) => {
  if (err) {
    return console.log(err);
  }
  fs.readFile(B, 'utf8', (err, fileB) => {
    if (err) {
      return console.log(err);
    }
    fs.writeFileSync(C, fileA + fileB);
  });
});
