#!/usr/bin/node
const factorial = (n) => {
  if (Number.isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
};
console.log(factorial(parseInt(process.argv[2])));
