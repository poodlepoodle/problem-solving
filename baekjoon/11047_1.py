import sys

input = sys.stdin.readline

# N <= 10, K <= 10^8
N, K = map(int, input().rstrip().split())

coins = [int(input()) for _ in range(N)]

answer = 0

for idx in range(len(coins) - 1, -1, -1):
    answer += K // coins[idx]
    K %= coins[idx]

print(answer)
