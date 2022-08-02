#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (elem of list) {
    if (elem == searchElement) {
      count++;
    }
  }
  return (count);
};
