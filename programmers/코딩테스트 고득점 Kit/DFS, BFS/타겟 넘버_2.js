/* 프로그래머스 43165번: 타겟 넘버 (2회차) */

function solution(numbers, target) {
  let answer = 0;
  const q = [];
  let qPtr = 0;

  q.push([0, 0]);

  while (qPtr < q.length) {
    const [currentIdx, totalSum] = q[qPtr++];

    if (currentIdx === numbers.length - 1) {
      if (totalSum + numbers[currentIdx] === target) answer++;
      if (totalSum - numbers[currentIdx] === target) answer++;
      continue;
    }

    q.push([currentIdx + 1, totalSum + numbers[currentIdx]]);
    q.push([currentIdx + 1, totalSum - numbers[currentIdx]]);
  }

  return answer;
}
