#!/usr/bin/node

const args = process.argv[2];

if (typeof args === 'undefined') {
  console.log('No argument');
} else {
  console.log(args);
}
