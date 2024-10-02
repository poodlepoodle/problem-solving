# 백준 1374번: 강의실 (2회차)

import heapq
import sys

input = sys.stdin.readline

# N <= 10^5
N = int(input())
lectures = [list(map(int, input().rstrip().split())) for _ in range(N)]
lectures.sort(key=lambda x:(x[1], x[2]))
runnings = []
answer = 0

for lecture in lectures:
    _, start, end = lecture

    while runnings and runnings[0] <= start:
        heapq.heappop(runnings)

    heapq.heappush(runnings, end)
    answer = max(answer, len(runnings))

print(answer)
