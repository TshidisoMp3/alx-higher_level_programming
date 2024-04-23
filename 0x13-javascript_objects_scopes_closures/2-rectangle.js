#!/usr/bin/node
// Defines a class Rectangle that defines a rectangle with constructor of w and h were w and h are equal to 0 or not a positive integer

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
