# 백준 14888번: 연산자 끼워넣기 (2회차)

from itertools import permutations
import sys

input = sys.stdin.readline

# N <= 11
N = int(input())
numbers = list(map(int, input().rstrip().split()))
pluses, minuses, muls, divs = map(int, input().rstrip().split())

operators = []
operators.extend('+' * pluses)
operators.extend('-' * minuses)
operators.extend('*' * muls)
operators.extend('/' * divs)

# 모든 연산자 조합 -> N! = 39916800 < 10^9
# 각 연산자 조합에 따른 수식 계산 -> O(N)
# 포인트: '순열'이므로 겹치는 건 제외해야 함

min_answer, max_answer = int(1e9), -int(1e9)
for operators in set(permutations(operators)):
    answer = numbers[0]
    for i in range(N - 1):
        op = operators[i]
        number = numbers[i + 1]
        if op == '+':
            answer += number
        elif op == '-':
            answer -= number
        elif op == '*':
            answer *= number
        elif op == '/':
            if answer * number < 0:
                answer = -(abs(answer) // abs(number))
            else:
                answer = answer // number
    min_answer = min(min_answer, answer)
    max_answer = max(max_answer, answer)

print(max_answer)
print(min_answer)
