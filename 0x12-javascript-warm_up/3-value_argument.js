#!/usr/bin/node

const arg = process.argv.length;
let i;

if (arg === 2) {
  console.log('No argument');
} else {
  for (i = 2; i < arg; i++) {
    console.log(process.argv[i]);
  }
}
