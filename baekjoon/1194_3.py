# 백준 1194번: 달이 차오른다, 가자. (3회차)

from collections import deque
import sys

input = sys.stdin.readline

# 빈 칸: 언제나 이동할 수 있다. ('.')
# 벽: 절대 이동할 수 없다. ('#')
# 열쇠: 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. ('a', 'b', 'c', 'd', 'e', 'f')
# 문: 대응하는 열쇠가 있을 때만 이동할 수 있다. ('A', 'B', 'C', 'D', 'E', 'F')
# 민식이의 현재 위치: 빈 곳이고, 민식이가 현재 서 있는 곳이다. ('0')
# 출구: 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. ('1')

# N, M <= 50
N, M = map(int, input().rstrip().split())

maps = [list(input().rstrip()) for _ in range(N)]

q = deque()
visited = [[[False for _ in range(64)] for _ in range(M)] for _ in range(N)]

for r in range(N):
    for c in range(M):
        if maps[r][c] == '0':
            maps[r][c] = '.'
            q.append((r, c, 0, 0))
            visited[r][c][0] = True

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
answer = -1

while q:
    r, c, keys, moved = q.popleft()

    if maps[r][c] == '1':
        answer = moved
        break
    elif maps[r][c] in ['a', 'b', 'c', 'd', 'e', 'f']:
        keys |= (1 << (ord(maps[r][c]) - ord('a')))

    for dr, dc in moves:
        if 0 <= r + dr < N and 0 <= c + dc < M:
            if maps[r + dr][c + dc] in ['A', 'B', 'C', 'D', 'E', 'F']:
                if keys & (1 << (ord(maps[r + dr][c + dc]) - ord('A'))):
                    if not visited[r + dr][c + dc][keys]:
                        q.append((r + dr, c + dc, keys, moved + 1))
                        visited[r + dr][c + dc][keys] = True
            elif maps[r + dr][c + dc] != '#':
                if not visited[r + dr][c + dc][keys]:
                    q.append((r + dr, c + dc, keys, moved + 1))
                    visited[r + dr][c + dc][keys] = True

print(answer)
