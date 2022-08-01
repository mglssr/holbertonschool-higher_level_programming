#!/usr/bin/node
const x = process.argv;
let a = '';
let b = '';
if (x.length <= 2) {
  a = 'undefined';
  b = 'undefined';
} else if (x.length < 4) {
  a = x[2];
  b = 'undefined';
} else {
  a = x[2];
  b = x[3];
}
console.log(a + ' ' + 'is' + ' ' + b);
