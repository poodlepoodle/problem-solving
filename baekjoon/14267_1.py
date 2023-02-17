from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

def input(): return sys.stdin.readline().rstrip()

# n, m은 최대 10^5
# 전부 DFS하게 되면 시간 초과 발생할 것으로 보임
n, m = map(int, input().split())

graph = defaultdict(list)

links = list(map(int, input().split()))
for i in range(1, len(links) + 1):
    graph[links[i - 1]].append(i)

goods = [0] * (n + 1)

def give_good(i, w):
    goods[i] += w

    for jjol in graph[i]:
        # 자기한테 온 칭찬을 전해줌
        give_good(jjol, goods[i])

for _ in range(m):
    i, w = map(int, input().split())
    
    goods[i] += w

give_good(1, 0)

print(*goods[1:])
