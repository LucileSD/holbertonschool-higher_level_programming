#!/usr/bin/node
/**
 * concats 2 files
 */
const fs = require('fs');

const A = process.argv[2];
const B = process.argv[3];
const C = process.argv[4];

fs.writeFileSync(C, fs.readFileSync(A) + fs.readFileSync(B));
