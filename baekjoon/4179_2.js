/* 백준 4179번: 불! */

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
let inputPtr = 0;
const input = () => lines[inputPtr++];

const [N, M] = input()
  .split(' ')
  .map((v) => +v);
const maze = Array.from({ length: N }, () => input().split(''));

const q = [];
const visited = Array.from({ length: N }, () => Array(M).fill(0));
let answer = -1;
let jr = -1;
let jc = -1;

for (let r = 0; r < N; r++) {
  for (let c = 0; c < N; c++) {
    if (maze[r][c] === 'J') {
      jr = r;
      jc = c;
    } else if (maze[r][c] === 'F') {
      q.push(['F', r, c, 1]);
      visited[r][c] = -1;
      maze[r][c] = '#';
    }
  }
}
q.push(['J', jr, jc, 1]);
visited[jr][jc] = 1;

const isJihoonExited = (r, c) =>
  r === 0 || r === N - 1 || c === 0 || c === M - 1;
const directions = [
  [-1, 0],
  [1, 0],
  [0, -1],
  [0, 1],
];

while (q.length > 0) {
  const [type, r, c, cnt] = q.shift();

  if (type === 'J') {
    if (isJihoonExited(r, c)) {
      answer = cnt;
      break;
    }

    directions.forEach(([dr, dc]) => {
      if (maze[r + dr][c + dc] !== '#' && visited[r + dr][c + dc] === 0) {
        q.push(['J', r + dr, c + dc, cnt + 1]);
        visited[r + dr][c + dc] = 1;
      }
    });
  } else if (type === 'F') {
    directions.forEach(([dr, dc]) => {
      if (
        0 <= r + dr &&
        r + dr < N &&
        0 <= c + dc &&
        c + dc < M &&
        maze[r + dr][c + dc] !== '#' &&
        visited[r + dr][c + dc] >= 0
      ) {
        q.push(['F', r + dr, c + dc]);
        visited[r + dr][c + dc] = -1;
      }
    });
  }
}

console.log(answer !== -1 ? answer : 'IMPOSSIBLE');
