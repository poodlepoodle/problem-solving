# 백준 12893번: 적의 적

from collections import defaultdict
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

# N <= 2 * 10^3
# M <= 10^6
N, M = map(int, input().rstrip().split())

# 접근
#   - 너무 대표적인 이분 그래프(Bipartite Graph) 문제

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A - 1].append(B - 1)
    graph[B - 1].append(A - 1)

visited = [0 for _ in range(N)]
answer = True

def dfs(current, color):
    global answer
    if not answer: return

    for _next in graph[current]:
        if not visited[_next]:
            visited[_next] = color * -1
            dfs(_next, color * -1)
        elif visited[_next] == color:
            answer = False
            return

for i in range(N):
    if not visited[i]:
        visited[i] = 1
        dfs(i, 1)

print(1 if answer else 0)
