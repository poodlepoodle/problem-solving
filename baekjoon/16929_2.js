/* 백준 16929번: Two Dots */

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
let inputPtr = 0;
const input = () => lines[inputPtr++];

// N, M <= 50
const [N, M] = input()
  .split(' ')
  .map((v) => +v);

const board = Array.from({ length: N }, () => Array.from(input()));
const visited = Array.from({ length: N }, () => Array(M).fill(-1));

let hasCycle = false;
const moves = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
const isValidPosition = (r, c) => 0 <= r && r < N && 0 <= c && c < M;
const isVisited = (r, c) => visited[r][c] !== -1;

function dfs(r, c, cnt, mark) {
  //   console.log(r, c);
  moves.forEach(([dr, dc]) => {
    if (isValidPosition(r + dr, c + dc) && mark === board[r + dr][c + dc]) {
      if (isVisited(r + dr, c + dc) && cnt - visited[r + dr][c + dc] >= 3) {
        hasCycle = true;
        // console.log('found!', r + dr, c + dc);
        return;
      }
      if (!isVisited(r + dr, c + dc)) {
        visited[r + dr][c + dc] = cnt + 1;
        dfs(r + dr, c + dc, cnt + 1, mark);
      }
    }
  });
}

for (let r = 0; r < N; r++) {
  for (let c = 0; c < M; c++) {
    if (!isVisited(r, c)) {
      //   console.log('* start from:', [r, c], board[r][c]);
      visited[r][c] = 0;
      dfs(r, c, 0, board[r][c]);
    }
  }
}

console.log(hasCycle ? 'Yes' : 'No');
