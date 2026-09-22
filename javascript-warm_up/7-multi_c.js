#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let str = '';
  for (let i = 0; i < num; i++) {
    str += 'C is fun\n';
  }
  console.log(str.trim());
}
