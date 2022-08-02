#!/usr/bin/node
/**
 *  a class Rectangle that defines a rectangle
 */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const sign = 'X';
    let line;
    for (line = 0; line < this.height; line++) {
      console.log(sign.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
