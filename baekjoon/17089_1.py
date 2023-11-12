# 백준 17089번: 세 친구

from collections import defaultdict
import sys

input = sys.stdin.readline

# N, M <= 4 * 10^3
N, M = map(int, input().rstrip().split())

friends = defaultdict(list)
num_friends = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().rstrip().split())

    friends[A].append(B)
    num_friends[A] += 1
    friends[B].append(A)
    num_friends[B] += 1

answer = int(1e9)

for A in range(1, N + 1):
    # print(A)
    for B in friends[A]:
        # print('->', B)

        for C in friends[B]:
            # print('-> -> ', C)

            if C in friends[A]:
                answer = min(answer, num_friends[A] + num_friends[B] + num_friends[C] - 6)

    # print()

print(answer if answer != int(1e9) else -1)
