#!/usr/bin/node
const axios = require('axios').default;
const argv = process.argv;
const fs = require('fs');
axios.get(argv[2])
  .then(function (response) {
    fs.writeFile(argv[3], response.data, err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
