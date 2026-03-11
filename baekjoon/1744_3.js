/* 백준 1744번 수 묶기 (3회차) */

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
let ptr = 0;
const input = () => lines[ptr++];

// N <= 50
const N = Number(input());

// -10^3 <= numbers[i] <= 10^3
const numbers = Array.from({ length: N }, () => Number(input()));
numbers.sort((a, b) => a - b);

// 포인트
// 1. 수열의 모든 수는 묶거나 묶지 않을 수 있음
// 2. 묶은 경우는 2개를 곱해서 더함

// 관찰 포인트
// 1. 음수는 두 개를 곱해서 더하는 게 나음
// 2. -1, 0, 1, 음수, 양수를 나누는 게 좋을 듯

let answer = 0;

// 모든 양수 곱해서 빼기
while (numbers.length >= 2 && numbers[numbers.length - 2] > 1) {
  answer += numbers[numbers.length - 2] * numbers[numbers.length - 1];
  numbers.pop();
  numbers.pop();
}
// 1은 무조건 더하는 게 이득
while (numbers.length > 0 && numbers[numbers.length - 1] > 0) {
  answer += numbers.pop();
}
// 0은 개수만 세주고 배열에서 전부 제거
let zero_cnt = 0;
while (numbers.length > 0 && numbers[numbers.length - 1] === 0) {
  zero_cnt++;
  numbers.pop();
}

// 모든 음수 곱해서 빼기
numbers.reverse();

while (numbers.length >= 2 && numbers[numbers.length - 2] <= -1) {
  answer += numbers[numbers.length - 2] * numbers[numbers.length - 1];
  numbers.pop();
  numbers.pop();
}
while (numbers.length > 0 && zero_cnt > 0) {
  numbers.pop();
  zero_cnt--;
}
numbers.forEach((number) => {
  answer += number;
});

// console.log(numbers);
console.log(answer);
