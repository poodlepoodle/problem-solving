from collections import defaultdict, deque
import sys

def input(): return sys.stdin.readline().rstrip()

# N의 최대 10^4, M은 최대 10^6
N, M = map(int, input().split())

trust = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    trust[B].append(A)

def hack(current):
    stack = deque()
    visited = [False] * (N + 1)

    stack.append(current)
    visited[current] = True

    cnt = 0

    while stack:
        com = stack.pop()

        for next_com in trust[com]:
            if not visited[next_com]:
                stack.append(next_com)
                cnt += 1
                visited[next_com] = True

    return cnt

answer = []
answer_cnt = 1

for i in range(1, N + 1):
    cnt = hack(i)

    if answer_cnt < cnt:
        answer = [i]
        answer_cnt = cnt
    elif answer_cnt == cnt:
        answer.append(i)

print(*answer)
