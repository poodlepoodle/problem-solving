# 백준 2212번: 센서

import sys

input = sys.stdin.readline

# N <= 10^4
N = int(input())

# K <= 10^3
K = int(input())

censors = list(map(int, input().rstrip().split()))
censors.sort()

distances = []
for i in range(1, len(censors)):
    distances.append(censors[i] - censors[i - 1])
distances.sort()

if K == 1:
    print(sum(distances))
else:
    print(sum(distances[:-(K - 1)]))
