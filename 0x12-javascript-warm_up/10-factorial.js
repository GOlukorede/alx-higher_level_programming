#!/usr/bin/node

const [, , ...args] = process.argv;
const a = parseInt(args[0]);

const fact = a => {
  if (!a) return 1;
  if (a <= 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
};

const test = fact(a);
console.log(test);
