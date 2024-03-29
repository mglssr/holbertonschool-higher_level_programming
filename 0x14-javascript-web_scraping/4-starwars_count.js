#!/usr/bin/node
const axios = require('axios').default;
const argv = process.argv;
axios.get(argv[2])
  .then(function (response) {
    const results = response.data.results;
    const ch = [];
    results.forEach(element => ch.push(element.characters));
    let i = 0;
    let count = 0;
    while (i < ch.length) {
      let p = 0;
      while (p < ch[i].length) {
        if (ch[i][p].includes('18')) {
          count++;
        }
        p++;
      }
      i++;
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
