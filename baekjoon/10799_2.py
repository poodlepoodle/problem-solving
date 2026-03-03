# 백준 10799번: 쇠막대기 (2회차)

import sys

input = sys.stdin.readline

# len(pipe) <= 10^5
pipe = input().rstrip()

# 포인트
#   1. 레이저는 스틱의 시작과 끝 사이기만 하면 어느 지점이든 상관은 없음
#      -> 편의를 위해서는 스틱이 끝나기 직전(닫는 괄호)이라고 생각하는 게 좋을듯
#   2. 그냥 이녀석은 스택을 사랑함

top = -1
answer = 0
lazer = False

for letter in pipe:
    # print(letter)
    if letter == '(':
        top += 1
        lazer = True
    elif letter == ')':
        if lazer:
            answer += top
            lazer = False
        else:
            answer += 1
        top -= 1

    # print(top, answer)
    # print()

print(answer)
