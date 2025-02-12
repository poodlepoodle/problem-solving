/* 프로그래머스 43163번: 단어 변환 (2회차) */

function distanceBetweenWords(w1, w2) {
  let distance = 0;
  for (let idx = 0; idx < w1.length; idx++) {
    if (w1[idx] !== w2[idx]) distance++;
  }
  return distance;
}

function solution(begin, target, words) {
  const q = [];
  let qPtr = 0;
  const visited = {};

  q.push([0, begin]);
  visited[begin] = true;
  // console.log(q);

  while (qPtr < q.length) {
    const [step, current] = q[qPtr++];
    // console.log(step, current);

    for (let word of words) {
      if (visited[word]) continue;

      const distance = distanceBetweenWords(current, word);
      if (distance <= 1) {
        if (word === target) return step + 1;

        q.push([step + 1, word]);
        visited[word] = true;
      }
    }
  }

  return 0;
}
