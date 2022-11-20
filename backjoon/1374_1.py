import sys
import heapq

def input(): return sys.stdin.readline().rstrip()

# 강의 갯수 N 최대 10^5
N = int(input())

lectures = []
for _ in range(N):
    idx, start, end = map(int, input().split())
    heapq.heappush(lectures, (start, end))

runnings = []

start, end = heapq.heappop(lectures)
heapq.heappush(runnings, end)

answer = 1
need = 1

while lectures:
    start, end = heapq.heappop(lectures)

    # 가장 빨리 끝나는 강의의 종료시간보다 현재 강의의 시작시간이 커질 때까지 pop
    while runnings and runnings[0] <= start:
        heapq.heappop(runnings)
        need -= 1

    heapq.heappush(runnings, end)
    need += 1
    answer = max(answer, need)

print(answer)
