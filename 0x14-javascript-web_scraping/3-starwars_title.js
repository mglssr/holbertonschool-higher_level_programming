#!/usr/bin/node
const axios = require('axios').default;
const argv = process.argv;

axios.get('https://swapi-api.hbtn.io/api/films/' + argv[2])
  .then(function (response) {
    console.log(response.data.title);
  });
