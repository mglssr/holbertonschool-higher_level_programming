#!/usr/bin/node
const x = process.argv;
if (x.length <= 3) {
  console.log('0');
} else {
  x.sort((a, b) => a - b);
  console.log(x[x.length - 2]);
}
