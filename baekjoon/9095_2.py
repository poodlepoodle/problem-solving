# 백준 9095번: 1, 2, 3 더하기 (2회차)

import sys

input = sys.stdin.readline

# N <= 주어지지 않음...
N = int(input())

ways = [0 for _ in range(12)]
ways[1] = 1
ways[2] = 2
ways[3] = 4
ways[4] = 7

for i in range(5, 11 + 1):
    ways[i] = ways[i - 1] + ways[i - 2] + ways[i - 3]

for _ in range(N):
    number = int(input())
    print(ways[number])
