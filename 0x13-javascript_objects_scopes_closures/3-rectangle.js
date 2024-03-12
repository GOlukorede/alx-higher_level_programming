#!/usr/bin/node
/**
 * Check the parameters provided
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
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
