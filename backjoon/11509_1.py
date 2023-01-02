from collections import defaultdict
import sys

input = sys.stdin.readline

# 최대 10^6
N = int(input())

heights = list(map(int, input().rstrip().split()))

answer = 0
arrows = defaultdict(int)

for height in heights:
    # print(height)

    if arrows[height] > 0:
        arrows[height] -= 1
        arrows[height - 1] += 1
    else:
        answer += 1
        arrows[height - 1] += 1

    # print(arrows, answer)

print(answer)
