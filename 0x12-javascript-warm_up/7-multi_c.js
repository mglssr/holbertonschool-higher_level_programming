#!/usr/bin/node
const x = process.argv;
if (x.length <= 2 || isNaN(parseInt(x[2]))) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < parseInt(x[2])) {
    console.log('C is fun');
    i++;
  }
}
