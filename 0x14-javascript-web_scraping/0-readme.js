#!/usr/bin/node
// Read and prints content from file

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
