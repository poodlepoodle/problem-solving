/* 백준 14267번: 회사 문화 1 */

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
let inputPtr = 0;
const input = () => lines[inputPtr++];

// N: 직원 수, M: 칭찬 수 <= 10^5
const [N, M] = input()
  .split(' ')
  .map((v) => +v);

const childs = {};
const parents = input()
  .split(' ')
  .map((v) => +v);
parents.forEach((parent, idx) => {
  if (parent === -1) return;
  childs[parent] = childs[parent] || [];
  childs[parent].push(idx + 1);
});
// console.log(childs);

const credits = Array(N + 1).fill(0);
for (let m = 0; m < M; m++) {
  const [i, w] = input()
    .split(' ')
    .map((v) => +v);

  credits[i] += w;
}

for (let ptr = 1; ptr <= N; ptr++) {
  const myCredit = credits[ptr];
  if (!!childs[ptr]) {
    childs[ptr].forEach((child) => {
      credits[child] += myCredit;
    });
  }
}
console.log(credits.slice(1).join(' '));
