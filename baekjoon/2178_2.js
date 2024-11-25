/* 백준 2178번: 미로 탐색 풀이 */

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
let inputPtr = 0;
const input = () => lines[inputPtr++];

const [N, M] = input()
  .split(' ')
  .map((v) => +v);
const maze = Array.from({ length: N }, () =>
  input()
    .split('')
    .map((v) => +v)
);

const q = [];
const visited = Array.from({ length: N }, () => Array(M).fill(false));
q.push([0, 0, 1]);
visited[0][0] = true;

const directions = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

while (q.length > 0) {
  const [r, c, cnt] = q.shift();

  if (r === N - 1 && c === M - 1) {
    console.log(cnt);
    break;
  }

  directions.forEach(([dr, dc]) => {
    if (0 <= r + dr && r + dr < N && 0 <= c + dc && c + dc < M) {
      if (maze[r + dr][c + dc] === 1 && !visited[r + dr][c + dc]) {
        q.push([r + dr, c + dc, cnt + 1]);
        visited[r + dr][c + dc] = true;
      }
    }
  });
}
