/* 프로그래머스 43162번: 네트워크 풀이 (2회차) */

function solution(n, computers) {
  let answer = 0;
  const graph = {};
  const visited = Array(n).fill(false);

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < i; j++) {
      if (computers[i][j]) {
        graph[i] = graph[i] ? [...graph[i], j] : [j];
        graph[j] = graph[j] ? [...graph[j], i] : [i];
      }
    }
  }

  function dfs(current) {
    visited[current] = true;

    for (const neighbor of graph[current] || []) {
      if (!visited[neighbor]) {
        dfs(neighbor);
      }
    }
  }

  for (let current = 0; current < n; current++) {
    if (!visited[current]) {
      dfs(current);
      answer++;
    }
  }

  return answer;
}
