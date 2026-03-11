# 백준 11659번: 구간 합 구하기 4

import sys

input = sys.stdin.readline

# N, M <= 10^5
N, M = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
prefixes = [0]
for number in numbers:
    prefixes.append(prefixes[-1] + number)

for _ in range(M):
    start, end = map(int, input().rstrip().split())
    print(prefixes[end] - prefixes[start - 1])
