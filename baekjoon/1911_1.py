# 백준 1911번: 흙길 보수하기

import sys

input = sys.stdin.readline

# N <= 10^4, L <= 10^6
N, L = map(int, input().rstrip().split())

pounds = [list(map(int, input().rstrip().split())) for _ in range(N)]
pounds.sort(key=lambda x:x[0])

# 그리디 전략: 한 웅덩이를 가리는 동안 다음 웅덩이까지 커버되는지를 확인

answer = 0
last = -1

for idx in range(N):
    current = pounds[idx]
    start = current[0]
    end = current[1] - 1
    # print(start, end)

    if last < start:
        last = start - 1
        while last < end:
            answer += 1
            last += L
            # print(last)
    elif last < end:
        while last < end:
            answer += 1
            last += L
            # print(last)
    else:
        pass

print(answer)
