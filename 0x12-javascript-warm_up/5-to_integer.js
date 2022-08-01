#!/usr/bin/node
const x = process.argv;
if (x.length <= 2 || isNaN(parseInt(x[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(x[2]));
}
