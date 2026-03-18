# 백준 7795번: 먹을 것인가 먹힐 것인가

import sys

input = sys.stdin.readline

# T <= ?
T = int(input())
for _ in range(T):
    # N, M <= 2 * 10^4
    N, M = map(int, input().rstrip().split())

    A = list(map(int, input().rstrip().split()))
    A.sort(reverse=True)
    B = list(map(int, input().rstrip().split()))
    B.sort(reverse=True)
    # print(A)
    # print(B)

    answer = 0
    ptr_A = 0
    ptr_B = 0

    # 시간복잡도 -> O(N + M)
    while ptr_A < N and ptr_B < M:
        a = A[ptr_A]
        b = B[ptr_B]

        if a > b:
            answer += M - ptr_B
            ptr_A += 1
        else:
            ptr_B += 1

    print(answer)
