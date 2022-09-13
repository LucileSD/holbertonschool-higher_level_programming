#!/usr/bin/node
/*
  prints the number of movies where the character “Wedge Antilles” is present
*/
const axios = require('axios');

const url = process.argv[2];

axios.get(url)
  .then(response => {
    let count = 0;
    for (const film of response.data.results) {
      for (const character of film.characters) {
        if (character.includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch(err => console.log(err));
