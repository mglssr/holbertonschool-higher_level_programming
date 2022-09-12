#!/usr/bin/node
const axios = require('axios').default;
const argv = process.argv;
var dict = {};
let users = 0
axios.get("https://jsonplaceholder.typicode.com/users")
  .then(function (resp) {
    users = resp.data.length
    let i = 1
    while (i <= users){
        axios.get(argv[2] + "?userId=" + i + "&completed=true")
          .then(function(response) {
            console.log(response.data.length)
        });
        i++;
    }
    console.log(dict)
});