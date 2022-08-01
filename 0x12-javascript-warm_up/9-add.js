#!/usr/bin/node
function add (a, b) {
  const c = Number(a) + Number(b);
  return (c);
}
const x = process.argv;
if (x.length <= 3) {
  console.log('NaN');
} else {
  const a = x[2];
  const b = x[3];
  console.log(add(a, b));
}
