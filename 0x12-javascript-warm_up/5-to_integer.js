#!/usr/bin/node

const [, , ...args] = process.argv;
const number = parseFloat(args[0]);
if (Number.isFinite(number)) {
  const test = Math.trunc(number);
  console.log(`My number: ${test}`);
} else {
  console.log('Not a number');
}
