from collections import deque
import sys

input = sys.stdin.readline

# 방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미
directions = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

q = deque()
fishes = []
for _ in range(4):
    a0, b0, a1, b1, a2, b2, a3, b3 = map(int, input().rstrip().split())
    row = []
    row.append((a0, b0 - 1))
    row.append((a1, b1 - 1))
    row.append((a2, b2 - 1))
    row.append((a3, b3 - 1))
    fishes.append(row)
