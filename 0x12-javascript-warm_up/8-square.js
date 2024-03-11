#!/usr/bin/node

const [, , ...args] = process.argv;

const num = Number.parseInt(args[0]);
if (num) {
  let i = 0;
  while (i < num) {
    const x = 'x';
    const rep = x.repeat(num);
    console.log(rep);
    i++;
  }
} else {
  console.log('Missing size');
}
