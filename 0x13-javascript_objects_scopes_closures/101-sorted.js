#!/usr/bin/node
/**
 * imports a dictionary of occurrences by user id and computes a dictionary
 * of user ids by occurrence
 */
const object = require('./101-data.js').dict;
const newDict = {};
for (const [key, value] of Object.entries(object)) {
  if (!newDict[value]) { newDict[value] = []; }
  newDict[value].push(key);
}
console.log(newDict);
