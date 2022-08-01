#!/usr/bin/node
/**
 * prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */
if (!process.argv[2]) console.log('Not a number');
else if (process.argv[2]) {
  if (isNaN(process.argv[2])) console.log('Not a number');
  else console.log(parseInt(process.argv[2]));
}
