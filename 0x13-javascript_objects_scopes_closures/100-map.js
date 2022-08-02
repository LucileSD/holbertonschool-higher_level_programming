#!/usr/bin/node
/**
 *  imports an array and computes a new array
 */
const list = require('./100-data').list;
const newArray = [];
list.map((element, index) => { return newArray.push(element * index); });
console.log(list);
console.log(newArray);
