/* 프로그래머스 1844번: 게임 맵 최단거리 (2회차) */

function solution(maps) {
  const N = maps.length;
  const M = maps[0].length;
  const directions = [
    [0, -1],
    [0, 1],
    [1, 0],
    [-1, 0],
  ];

  const q = [];
  let qPtr = 0;
  const visited = Array.from({ length: N }, () => Array(M).fill(-1));

  q.push([0, 0, 1]);
  visited[0][0] = 1;

  while (qPtr < q.length) {
    const [r, c, step] = q[qPtr++];
    // console.log(r, c, step);

    for (let [dr, dc] of directions) {
      if (
        0 <= r + dr &&
        r + dr < N &&
        0 <= c + dc &&
        c + dc < M &&
        maps[r + dr][c + dc] === 1 &&
        visited[r + dr][c + dc] === -1
      ) {
        if (r + dr === N - 1 && c + dc === M - 1) return step + 1;

        q.push([r + dr, c + dc, step + 1]);
        visited[r + dr][c + dc] = step + 1;
      }
    }
  }

  return -1;
}
