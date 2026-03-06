# 백준 1931번: 회의실 배정 (2회차)

import sys

input = sys.stdin.readline

# N <= 10^5
N = int(input())
meetings = [list(map(int, input().rstrip().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1], x[0]))

answer = 0
last_end = -1

for start, end in meetings:
    if last_end <= start:
        # print(start, end)
        last_end = end
        answer += 1

print(answer)
