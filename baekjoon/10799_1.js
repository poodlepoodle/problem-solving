/* 백준 10799번: 쇠막대기 */

const fs = require('fs');
const string = fs.readFileSync('/dev/stdin').toString().trim();

let answer = 0;
let working = 0;

for (let idx = 0; idx < string.length; idx++) {
  const item = string[idx];

  if (item === '(') {
    if (string[idx + 1] === ')') {
      answer += working;
      idx++;
      //   console.log('razor!', working, answer);
    } else {
      working++;
      //   console.log(working, answer);
    }
  } else {
    working--;
    answer++;
    // console.log(working, answer);
  }
}

console.log(answer);
