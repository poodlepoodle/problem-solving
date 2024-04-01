const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const range = (N) => Array.from(Array(N).keys());

const [N, M] = input[0].split(' ').map((item) => parseInt(item));
let [r, c, d] = input[1].split(' ').map((item) => parseInt(item));
let maps = input
  .slice(2)
  .map((line) => line.split(' ').map((item) => parseInt(item)));

const directions = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

let answer = 0;
let clean_around = false;

while (true) {
  if (maps[r][c] === 0) {
    maps[r][c] = 2;
    answer++;
  }

  clean_around = false;

  for (let _ of range(4)) {
    d = (d + 3) % 4;
    const [dr, dc] = directions[d];

    if (maps[r + dr][c + dc] === 0) {
      r += dr;
      c += dc;
      clean_around = true;
      break;
    }
  }

  if (!clean_around) {
    const [dr, dc] = directions[(d + 2) % 4];
    if (maps[r + dr][c + dc] !== 1) {
      r += dr;
      c += dc;
    } else {
      break;
    }
  }
}

console.log(answer);
