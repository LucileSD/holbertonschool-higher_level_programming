#!/usr/bin/node
/**
 * a class Square that defines a square and inherits from
 * Rectangle of 4-rectangle.js
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) { c = 'X'; }
    let line;
    for (line = 0; line < this.width; line++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
