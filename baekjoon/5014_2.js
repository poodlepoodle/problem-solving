// 5014번: 스타트링크 (2회차)

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

// F, S, G, U, D 입력 (1 ≤ S, G ≤ F ≤ 10^6, 0 ≤ U, D ≤ 10^6)
const [F, S, G, U, D] = input.split(' ').map((item) => parseInt(item));

let q = [];
let visited = Array(F + 1).fill(false);

q.push([S, 0]);
visited[S] = true;

const moves = [U, -D];
let answer = 'use the stairs';

while (q.length > 0) {
  const [current, level] = q.shift();

  if (current === G) {
    answer = level;
    break;
  }

  moves.forEach((step) => {
    if (1 <= current + step && current + step <= F) {
      if (!visited[current + step]) {
        visited[current + step] = true;
        q.push([current + step, level + 1]);
      }
    }
  });
}

console.log(answer);
