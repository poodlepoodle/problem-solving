# 백준 4889번: 안정적인 문자열

import sys

input = sys.stdin.readline

T = 0

while True:
    string = input().rstrip()
    if string[0] == '-': break
    T += 1

    # 1. 문자열의 길이 <= 2000
    # 2. 문자열의 길이는 항상 짝수

    stack = []
    answer = 0

    for letter in string:
        # print(letter)
        if letter == '{':
            stack.append(letter)
        elif letter == '}':
            if len(stack) > 0:
                stack.pop()
            else:
                answer += 1
                stack.append('{')
        # print(stack)

    answer += len(stack) // 2
    print(f'{T}. {answer}')
