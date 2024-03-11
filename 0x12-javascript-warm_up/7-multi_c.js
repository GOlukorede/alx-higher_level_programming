#!/usr/bin/node

const [, , ...args] = process.argv;

const num = Number.parseInt(args[0]);

if (Number.isFinite(num)) {
  const test = 'C is fun';
  let i = 0;
  while (i < num) {
    console.log(test);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
