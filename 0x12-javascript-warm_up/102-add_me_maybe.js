#!/usr/bin/node
/**
 * increments and calls a function
 */
exports.addMeMaybe = function (number, theFunction) {
  number += 1;
  return (theFunction(number));
};
