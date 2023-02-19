from collections import defaultdict, deque
import sys

input = sys.stdin.readline

# N <= 10^4, M <= 10^5
N, M = map(int, input().rstrip().split())

bridges = defaultdict(dict)
for _ in range(M):
    A, B, limit = map(int, input().rstrip().split())

    bridges[A][B] = limit
    bridges[B][A] = limit

start, end = map(int, input().rstrip().split())

def bfs(weight):
    q = deque([start])
    visited = [False for _ in range(N + 1)]

    while q:
        current = q.popleft()

        if current == end:
            return True
    
        for neighbor, limit in bridges[current].items():
            if not visited[neighbor] and limit >= weight:
                visited[neighbor] = True
                q.append(neighbor)

    return False

lower_bound, upper_bound = 1, int(1e9)
answer = 0

while lower_bound <= upper_bound:
    # print(lower_bound, upper_bound)

    middle = int((lower_bound + upper_bound) / 2)

    if bfs(middle):
        lower_bound = middle + 1
        answer = middle
    else:
        upper_bound = middle - 1

print(answer)
