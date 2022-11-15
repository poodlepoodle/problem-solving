import sys
from collections import defaultdict

sys.setrecursionlimit(10**5)

def input(): return sys.stdin.readline().rstrip()

K = int(input())

def dfs(current, sign):
    visited[current] = sign

    for neighbor in edge[current]:
        # 1. 아직 방문하지 않은 경우는
        if visited[neighbor] == False:
            # 다른 집합으로 분류해서 DFS 수행
            if not dfs(neighbor, -sign):
                return False
        # 2. 방문한 경우는
        else:
            # 반대 집합이면 통과하고 아닌 경우는 False 리턴
            if visited[neighbor] == sign:
                return False

    return True

for _ in range(K):
    V, E = map(int, input().split())

    edge = defaultdict(list)
    for _ in range(E):
        A, B = map(int, input().split())
        
        if A in edge.keys():
            edge[A].append(B)
        else:
            edge[A] = [B]
        if B in edge.keys():
            edge[B].append(A)
        else:
            edge[B] = [A]

    visited = [False] * (V + 1)

    answer = 'YES'
    for v in range(V):
        if visited[v] == False:
            if not dfs(v, 1):
                answer = 'NO'

    print(answer)
