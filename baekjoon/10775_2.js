/* 백준 10775번: 공항 (2회차) */

const fs = require('fs');
const lines = fs
  .readFileSync('/dev/stdin', { encoding: 'utf-8' })
  .toString()
  .split('\n');
let ptr = 0;
const input = () => lines[ptr++];

// GATES, PLANES <= 10^5
const GATES = Number(input());
const PLANES = Number(input());

// 포인트
// - 주어진 Gi는 해당 비행기를 1번 ~ Gi번 게이트 중 하나에 도킹 가능하다는 말,
// - 앞에 어떤 비행기가 오든 뒤의 비행기를 감안하려면 최대한 게이트 번호가 큰 곳에 도킹시키는 게 이득 아닌가...?
// 시간복잡도 계산
// 1. 모든 비행기에 대해서 체크 -> 10^5
// 2. 각 비행기마다 모든 게이트 체크 -> 10^5
// -> 그냥 돌리면 안 된다.. 근데 모든 비행기에 대해 체크는 줄일 수 없으므로 게이트 체크에서 logN 이내로 줄여야 함
// 아이디어
// Gi = 5, 5, 4, 1인 비행기가 있다고 할 때, 맨 처음 Gi=5인 비행기가 5번 게이트에 도킹하면
//   사실상 이제 앞으로의 Gi=5인 모든 비행기는 Gi=4인 것이나 다름없음

dockings = Array.from({ length: GATES + 1 }, () => false);
parents = Array.from({ length: GATES + 1 }, (_, idx) => idx);

function find(x) {
  if (x === parents[x]) return x;
  parents[x] = find(parents[x]);
  return parents[x];
}

function union(a, b) {
  const A = find(a);
  const B = find(b);

  if (A < B) parents[B] = A;
  else if (A > B) parents[A] = B;
}

let answer = 0;
for (const _ of Array.from({ length: PLANES })) {
  const Gi = Number(input());
  //   console.log('Gi:', Gi);
  let gate = find(Gi);
  //   console.log('MAX_GATE:', gate);

  while (true) {
    if (!dockings[gate]) {
      dockings[gate] = true;
      union(Gi, gate - 1);
      break;
    }

    gate--;
    if (gate < 1) break;
  }

  if (!gate) break;
  answer += 1;

  //   console.log(dockings.slice(1).map((v) => (v ? 'O' : '.')));
  //   console.log(parents.slice(1));
  //   console.log();
}

console.log(answer);
