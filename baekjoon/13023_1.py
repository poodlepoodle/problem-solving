# 13023번: ABCDE

from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# 사람의 수 N, 친구 관계의 수 M <= 2 * 10^3
N, M = map(int, input().rstrip().split())

# Union-Find 알고리즘을 통해 친구 관계가 존재하면 같은 그룹으로 분류하면 어떨까...
# -> 테스트 케이스 3을 보면, A - B가 친구라고 해서 B - C가 친구일 때 C가 A와 친구는 아님.

# 고민 1: A-B가 친구일 때, B에서 친구로 선택할 수 있는 범위에는 A가 제외되어야 함.
# 고민 2: 그냥 돌리면 시간초과 남

friends = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    friends[A].append(B)
    friends[B].append(A)

visited = [False] * (N + 1)
answer = False

def dfs(current, depth):
    # print(f"dfs({current}, {depth})")

    if depth >= 4:
        global answer
        answer = True
        return

    for neighbor in friends[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, depth + 1)
            visited[neighbor] = False

for idx in range(N):
    visited[idx] = True
    dfs(idx, 0)
    visited[idx] = False

    if answer: break

print(1 if answer else 0)
