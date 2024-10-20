/* 백준 5052번: 전화번호 목록 (2회차) */

const fs = require('fs');
const line = fs.readFileSync('/dev/stdin').toString().split('\n');
let pointer = 0;
const input = () => line[pointer++];

const T = parseInt(input());
for (let t = 0; t < T; t++) {
  const N = parseInt(input());
  const numbers = Array.from({ length: N }, () => input().toString());
  console.log(solution(N, numbers));
}

function solution(N, numbers) {
  const trie = {};

  for (let number of numbers) {
    let current = trie;
    // console.log(number);

    for (let idx = 0; idx < number.length; idx++) {
      const letter = number[idx];

      if (!current[letter]) current[letter] = {};
      else if (current[letter]['*'] === true) return 'NO';

      current = current[letter];
    }

    if (Object.keys(current).length > 0) return 'NO';

    // console.log(JSON.stringify(current, null, 2));
    current['*'] = true;
    // console.log(JSON.stringify(current, null, 2));
  }

  return 'YES';
}
