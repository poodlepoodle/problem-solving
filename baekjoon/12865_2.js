// 12865번: 평범한 배낭 (2회차)

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, K] = input[0].split(' ').map(Number);
const things = [
  0,
  ...input.slice(1, N + 1).map((line) => line.split(' ').map(Number)),
];

dp = Array.from({ length: K + 1 }, () => Array(N + 1).fill(0));

for (let i = 1; i <= K; i++) {
  for (let j = 1; j <= N; j++) {
    const [W, V] = things[j];

    dp[i][j] = dp[i][j - 1];

    if (i - W >= 0)
      dp[i][j] =
        dp[i - W][j - 1] + V > dp[i][j] ? dp[i - W][j - 1] + V : dp[i][j];
  }
}

console.log(dp[K][N]);
