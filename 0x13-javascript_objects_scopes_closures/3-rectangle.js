#!/usr/bin/node
/**
 * Check the parameters provided
 */

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const a = 'x'.repeat(this.width);
    let i = 0;
    while (i < this.height) {
      console.log(a);
      i++;
    }
  }
}

module.exports = Rectangle;
