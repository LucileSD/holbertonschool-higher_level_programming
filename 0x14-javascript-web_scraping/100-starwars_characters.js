#!/usr/bin/node
/*
  prints all characters of a Star Wars movie
*/
const axios = require('axios');

axios({
  method: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
})
  .then((response) => {
    for (const character of response.data.characters) {
      axios.get(character)
        .then(res => {
          console.log(res.data.name);
        });
    }
  })
  .catch((err) => console.log(err));
