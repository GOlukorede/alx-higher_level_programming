#!/usr/bin/node

const [, , ...args] = process.argv;
const a = Number(args[0]);
const b = Number(args[1]);

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
add(a, b);
