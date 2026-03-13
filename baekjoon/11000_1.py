# 백준 11000번: 강의실 배정

import heapq
import sys

input = sys.stdin.readline

# N <= 2 * 10^5
N = int(input())

# 0 <= start, end <= 10^9
classes = [list(map(int, input().rstrip().split())) for _ in range(N)]
classes.sort()

# 기억나는 것들
#   - 이 유형의 그리디에서는 최소 힙에 시작 시간인지 종료 시간 중 하나만 쭉 넣었던 걸로 기억함
runnings = []

answer = 0
for start, end in classes:
    if runnings and runnings[0] <= start:
        heapq.heappop(runnings)
    heapq.heappush(runnings, end)

    answer = max(answer, len(runnings))

print(answer)
