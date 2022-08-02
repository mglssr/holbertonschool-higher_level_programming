#!/usr/bin/node
let callnum = 0;

exports.logMe = function (item) {
  console.log(callnum + ' : ' + item);
  callnum++;
};
