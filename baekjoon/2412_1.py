from collections import deque, defaultdict
import sys

input = sys.stdin.readline

# N은 최대 5 * 10^4, T는 최대 2 * 10^5
N, T = map(int, input().rstrip().split())

steps = defaultdict(list)
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    steps[y].append(x)

q = deque([(0, 0, 0)])

answer = False

while q:
    level, x, y = q.popleft()

    if y >= T:
        answer = level
        break

    # 이동할 수 있는 범위 내에 홈을 모두 계산
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            if x + dx in steps[y + dy]:
                steps[y + dy].remove(x + dx)
                q.append((level + 1, x + dx, y + dy))

    # print(steps)
    # print(q)
    # print()

print(answer if answer else -1)
