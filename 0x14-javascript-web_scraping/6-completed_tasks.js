#!/usr/bin/node
const argv = process.argv;
const axios = require('axios').default;

axios.get(argv[2])
.then(function (response) {
  const data = response.data;
  const dict = {};
  let i = 0
  while (i < data.length) {
    if (data[i].completed === true) {
      if (dict[data[i].userId] !== undefined) {
        dict[data[i].userId] = dict[data[i].userId] += 1;
      } else {
        dict[data[i].userId] = 1;
      }
    }
    i++;
  }
  console.log(dict);
}).catch(function (error) {
  console.log(`code: ${error.response.status}`);
});