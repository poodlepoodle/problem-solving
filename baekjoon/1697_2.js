// 1697번: 숨바꼭질
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString();

const [subin, sister] = input.split(' ').map((v) => +v);

MAX = 100000;

let q = [];
let visited = Array(MAX).fill(0);

q.push([subin, 0]);
visited[subin] = 1;

answer = -1;
q_ptr = 0;

while (q.length > 0) {
  const [current, level] = q[q_ptr++];

  if (current === sister) {
    answer = level;
    break;
  }

  const next_moves = [current + 1, current - 1, current * 2];

  for (let next of next_moves) {
    if (0 <= next && next <= MAX) {
      if (!visited[next]) {
        visited[next] = 1;
        q.push([next, level + 1]);
      }
    }
  }
}

console.log(answer);
