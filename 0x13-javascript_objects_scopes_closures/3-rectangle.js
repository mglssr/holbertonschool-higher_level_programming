#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    const ch = 'X';
    while (i < this.height) {
      console.log(ch.repeat(this.width));
      i++;
    }
  }
};
