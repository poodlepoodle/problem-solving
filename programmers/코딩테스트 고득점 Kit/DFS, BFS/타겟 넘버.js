/* 프로그래머스 43165번: 타겟 넘버 */

function caseSum(numbers, operators) {
  return (sum = numbers.reduce((sum, number, idx) => {
    return sum + operators[idx] * number;
  }, 0));
}

function solution(numbers, target) {
  let answer = 0;

  function dfs(current, end, operators) {
    // console.log(`dfs(${current}, ${end}, [${operators}])`);
    if (current === end) {
      const sum = caseSum(numbers, operators);
      return sum === target ? 1 : 0;
    }

    return (
      dfs(current + 1, end, [...operators, -1]) +
      dfs(current + 1, end, [...operators, 1])
    );
  }

  answer += dfs(-1, numbers.length - 1, []);

  return answer;
}
