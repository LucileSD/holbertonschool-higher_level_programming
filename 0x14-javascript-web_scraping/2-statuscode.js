#!/usr/bin/node
/* display the status code of a GET request */
const axios = require('axios');

axios({
  url: process.argv[2],
  method: 'GET'
})
  .then((response) => {
    console.log('code: ' + response.status);
  },
  (error) => {
    console.log('code: ' + error.response.status);
  });
