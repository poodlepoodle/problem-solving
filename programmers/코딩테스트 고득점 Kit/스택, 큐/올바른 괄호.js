/* 프로그래머스 12909번: 올바른 괄호 풀이 */

function solution(s) {
  const stack = [];

  for (let item of s) {
    if (item === ')') {
      if (stack.length === 0) return false;

      const recentItem = stack.pop();
      if (recentItem !== '(') return false;
    } else {
      stack.push(item);
    }
  }

  return stack.length > 0 ? false : true;
}
