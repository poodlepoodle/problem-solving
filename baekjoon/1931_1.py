import sys
import heapq

input = sys.stdin.readline

# N <= 10^5
N = int(input())

meetings = []

for _ in range(N):
    start, end = map(int, input().rstrip().split())

    heapq.heappush(meetings, (end, start))

answer = 0
current_end = -1

while meetings:
    end, start = heapq.heappop(meetings)

    if current_end <= start:
        answer += 1
        current_end = end

print(answer)
