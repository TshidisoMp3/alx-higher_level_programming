#!/usr/bin/node
// class of rectangle with constructor of w and h were w and h are equal to 0 or not a positive integer and methods print the reactangle with character X

module.exports = class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        [this.width, this.height] = [w, h];
      }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  };
  