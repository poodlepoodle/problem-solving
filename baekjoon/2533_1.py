from collections import defaultdict
import sys

input = sys.stdin.readline

# N <= 10^6
N = int(input())

friends = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, input().rstrip().split())

    friends[u].append(v)
    friends[v].append(u)

