/* 프로그래머스 12909번: 올바른 괄호 풀이 (2회차) */

function solution(s) {
  const stack = [];

  for (let letter of s) {
    if (letter === '(') stack.push(letter);
    else {
      if (stack.length === 0) return false;
      if (stack[stack.length - 1] !== '(') return false;
      stack.pop();
    }
  }

  return stack.length > 0 ? false : true;
}
