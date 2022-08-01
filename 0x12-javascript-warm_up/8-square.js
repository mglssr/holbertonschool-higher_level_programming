#!/usr/bin/node
const x = process.argv;
let i = 0;
const a = 'X';
if (x.length <= 2 || isNaN(parseInt(x[2]))) {
  console.log('Missing size');
} else {
  while (i < parseInt(x[2])) {
    console.log(a.repeat(parseInt(x[2])));
    i++;
  }
}
