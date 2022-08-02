#!/usr/bin/node
/**
 *  prints the number of arguments already printed and the new argument value
 */
let idx = 0;
exports.logMe = function (item) {
  console.log(idx + ': ' + item);
  idx += 1;
};
