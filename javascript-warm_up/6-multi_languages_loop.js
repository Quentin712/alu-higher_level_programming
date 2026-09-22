#!/usr/bin/node

const langs = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let str = '';

for (const lang of langs) {
  str += lang + '\n';
}

console.log(str.trim());
