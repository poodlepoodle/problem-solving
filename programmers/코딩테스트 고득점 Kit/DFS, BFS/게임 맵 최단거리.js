/* 프로그래머스 1844번: 게임 맵 최단거리 */

function solution(maps) {
  const N = maps.length;
  const M = maps[0].length;
  maps[N - 1][M - 1] = 2;

  const q = [];
  let q_ptr = 0;
  const visited = Array.from({ length: N }, () => Array(M).fill(false));

  const directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];

  q.push([0, 0, 1]);
  visited[0][0] = true;

  while (q_ptr < q.length) {
    const [r, c, cnt] = q[q_ptr++];

    for (let [dr, dc] of directions) {
      if (0 <= r + dr && r + dr < N && 0 <= c + dc && c + dc < M) {
        if (maps[r + dr][c + dc] === 2) {
          return cnt + 1;
        } else if (maps[r + dr][c + dc] && !visited[r + dr][c + dc]) {
          q.push([r + dr, c + dc, cnt + 1]);
          visited[r + dr][c + dc] = true;
        }
      }
    }
  }

  return -1;
}
