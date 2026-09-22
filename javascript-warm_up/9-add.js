#!/usr/bin/node

const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);

function add (num1, num2) {
  return num1 + num2;
}

console.log(add(a, b));
