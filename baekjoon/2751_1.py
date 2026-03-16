# 백준 2751번: 수 정렬하기 2

import heapq
import sys

input = sys.stdin.readline

heap = []

N = int(input())
for _ in range(N):
    heapq.heappush(heap, int(input()))

while heap:
    print(heapq.heappop(heap))
