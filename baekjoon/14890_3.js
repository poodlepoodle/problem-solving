/* 백준 14890번: 경사로 (3회차) */

const fs = require('fs');
const lines = fs
  .readFileSync('/dev/stdin')
  .toString()
  .split('\n')
  .map((l) => l.trim());
let ptr = 0;
const input = () => lines[ptr++];

// N <= 10^2
const [N, L] = input()
  .split(' ')
  .map((i) => +i);
const maps = Array.from({ length: N }, () =>
  input()
    .split(' ')
    .map((v) => +v)
);
// console.log(`N = ${N}, L = ${L}`);

const routes = [...maps];
for (let j = 0; j < N; j++) {
  const vertical_routes = [];
  for (let i = 0; i < N; i++) {
    vertical_routes.push(maps[i][j]);
  }
  routes.push(vertical_routes);
}

let answer = 0;
routes.forEach((blocks) => {
  //   console.log('------------------');
  //   console.log('blocks:', blocks);
  const visited = Array(N).fill(false);

  // 경사로를 놓는 2개 케이스 -> 올라가다 만나거나 내려가다 만나거나
  for (let i = 1; i < N; i++) {
    // console.log(`i: ${i}`);
    const diff = blocks[i] - blocks[i - 1];
    if (diff === 0) continue;
    if (Math.abs(diff) > 1) return;

    let cnt;
    // 올라가다 만난 경우는 이전 칸들을 조사
    if (diff === 1) {
      //   console.log('upper case');
      cnt = 0;

      for (let j = i - 1; j > i - L - 1; j--) {
        // console.log(`  j: ${j}`);
        if (blocks[j] !== blocks[i - 1] || visited[j]) {
          //   console.log(blocks[j] !== blocks[i], visited[j]);
          return;
        }

        visited[j] = true;
        cnt++;
      }
      //   console.log('  visited:', visited);

      if (cnt < L) return;
    }
    // 내려가다 만난 경우는 다음 칸들을 조사
    else if (diff === -1) {
      //   console.log('lower case');
      cnt = 0;

      for (let j = i; j < i + L; j++) {
        // console.log(`  j: ${j}`);
        if (blocks[j] !== blocks[i] || visited[j]) {
          //   console.log(blocks[j] !== blocks[i], visited[j]);
          return;
        }

        visited[j] = true;
        cnt++;
      }
      //   console.log('  visited:', visited);

      if (cnt < L) return;
    }
  }

  //   console.log('success');
  answer++;
});

console.log(answer);
