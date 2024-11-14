/* 백준 1406번: 에디터 */

const fs = require('fs');
const lines = fs.readFileSync('/dev/stdin').toString().split('\n');
let inputPtr = 0;
const input = () => lines[inputPtr++];

const leftStack = Array.from(input());
const rightStack = [];

// L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
// D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
// B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
//      삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만,
//      실제로 커서의 오른쪽에 있던 문자는 그대로임
// P $	$라는 문자를 커서 왼쪽에 추가함

const operate = {
  L: () => {
    if (leftStack.length > 0) rightStack.push(leftStack.pop());
  },
  D: () => {
    if (rightStack.length > 0) leftStack.push(rightStack.pop());
  },
  B: () => {
    if (leftStack.length > 0) leftStack.pop();
  },
  P: (newLetter) => {
    leftStack.push(newLetter);
  },
};

const commands = Number(input());

Array.from({ length: commands }).forEach(() => {
  const [command, operand] = input().split(' ');
  operate[command](operand);
  //   console.log(command, operand);
  //   console.log(leftStack, rightStack);
});

rightStack.reverse();
console.log(leftStack.join('') + rightStack.join(''));
