#!/usr/bin/node
const x = process.argv;
if (!x[2]) {
  console.log('No argument');
} else {
	console.log(x[2]);
}
