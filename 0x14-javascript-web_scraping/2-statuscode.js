#!/usr/bin/node
const axios = require('axios').default;
const argv = process.argv;

axios.get(argv[2])
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
