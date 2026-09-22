#!/usr/bin/node

const arg= process.arg[2];
const num= parseINT(arg, 10);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
