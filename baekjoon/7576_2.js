/* 7576번: 토마토(2차원) (2회차) */

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const range = (N) => Array.from(Array(N).keys());

const [M, N] = input[0].split(' ').map((item) => parseInt(item));
let maps = input
  .slice(1)
  .map((item) => item.split(' ').map((item) => parseInt(item)));

let q = [];
visited = Array.from({ length: N }, () => Array(M).fill(false));

for (let r of range(N)) {
  for (let c of range(M)) {
    if (maps[r][c] === 1) {
      q.push([r, c, 0]);
      visited[r][c] = true;
    }
  }
}

const moves = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

let answer = -1;
let q_ptr = 0;

while (q_ptr < q.length) {
  const [r, c, level] = q[q_ptr++];

  answer = level > answer ? level : answer;

  for (let [dr, dc] of moves) {
    if (0 <= r + dr && r + dr < N && 0 <= c + dc && c + dc < M) {
      if (maps[r + dr][c + dc] === 0 && !visited[r + dr][c + dc]) {
        q.push([r + dr, c + dc, level + 1]);
        visited[r + dr][c + dc] = true;
      }
    }
  }
}

let all_visited = true;

for (let r of range(N)) {
  for (let c of range(M)) {
    if (maps[r][c] === 0 && !visited[r][c]) {
      all_visited = false;
      break;
    }
  }
}

console.log(all_visited ? answer : -1);
