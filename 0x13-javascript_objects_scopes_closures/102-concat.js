#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destinationFile = process.argv[4];

const file1Content = fs.readFileSync(file1, 'utf-8');
const file2Content = fs.readFileSync(file2, 'utf-8');
const concatContent = file1Content + file2Content;

fs.writeFileSync(destinationFile, concatContent);

console.log(`Contents of ${file1} and ${file2} have been concatenated to ${destinationFile}.`);
