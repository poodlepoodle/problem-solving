# 백준 13164번: 행복 유치원 (2회차)

import sys

input = sys.stdin.readline

# N, K <= 3 * 10^5
N, K = map(int, input().rstrip().split())

kids = list(map(int, input().rstrip().split()))

differences = []
for idx in range(1, len(kids)):
    differences.append(kids[idx] - kids[idx - 1])

differences.sort()

if K == 1:
    print(sum(differences))
else:
    print(sum(differences[:-K + 1]))
