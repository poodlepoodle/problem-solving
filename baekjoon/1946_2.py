# 백준 1946번: 신입사원 (2회차)

import sys
import heapq

input = sys.stdin.readline

# 테스트 케이스 T <= 20
for _ in range(int(input())):
    # N <= 10^5
    N = int(input())

    applies = []
    for _ in range(N):
        rank_A, rank_B = map(int, input().rstrip().split())
        heapq.heappush(applies, (rank_A, rank_B))

    rank_A, rank_B = heapq.heappop(applies)
    highest_rank_B = rank_B
    passes = 1

    while applies:
        rank_A, rank_B = heapq.heappop(applies)

        if rank_B < highest_rank_B:
            passes += 1
            highest_rank_B = rank_B

    print(passes)
