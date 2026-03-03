/* 백준 1863번: 스카이라인 쉬운거 (2회차) */

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
let ptr = 0;
const input = () => lines[ptr++];

// N <= 5 * 10^4
const N = Number(input());
const stack = [];
let answer = 0;

Array.from({ length: N }, () => {
  const [x, y] = input()
    .split(' ')
    .map((n) => +n);
  //   console.log(x, y);

  while (stack.length > 0 && stack[stack.length - 1] > y) {
    answer++;
    stack.pop();
  }

  if (stack.length > 0 && stack[stack.length - 1] === y) return;
  if (y === 0) return;
  stack.push(y);
  //   console.log(answer, stack, '\n');
});

console.log(answer + stack.length);
