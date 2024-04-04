// 14501번: 퇴사

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const range = (N) => Array.from(Array(N).keys());

const N = parseInt(input[0]);
const arr = [
  0,
  ...input.slice(1).map((line) => line.split(' ').map((i) => +i)),
];

// console.log(N);
// console.log(arr);

// dp[i]: i번째 날까지 얻을 수 있는 최대 상담 이익
// dp[j] = max(dp[j], dp[i] + i번째 날에 시작하는 상담의 이익)

let dp = Array(N + 2).fill(0);

for (let i = 1; i <= N; i++) {
  //   console.log('i =', i);
  const [workdays, profit] = arr[i];

  for (let j = i + workdays; j <= N + 1; j++) {
    // console.log(`${dp[i]}(i = ${i}) + ${profit} vs ${dp[j]}(j = ${j})`);
    dp[j] = dp[i] + profit > dp[j] ? dp[i] + profit : dp[j];
  }

  //   console.log(dp.slice(1));
  //   console.log();
}

console.log(dp[N + 1]);
