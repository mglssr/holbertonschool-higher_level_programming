#!/usr/bin/node
function recursion (num) {
  if (num < 0) {
    return (-1);
  } else if (num === 0 || !num) {
    return (1);
  } else {
    return (num * recursion(num - 1));
  }
}
const x = process.argv;
console.log(recursion(x[2]));
