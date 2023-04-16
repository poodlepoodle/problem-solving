from collections import deque
import sys

input = sys.stdin.readline

# N, M <= 50
N, M = map(int, input().rstrip().split())

maps = [list(input().rstrip()) for _ in range(N)]

start_r, start_c = -1, -1
for r in range(N):
    for c in range(M):
        if maps[r][c] == '0':
            maps[r][c] = '.'
            start_r, start_c = r, c

q = deque()
visited = [[[1e9 for _ in range(2**6)] for _ in range(M)] for _ in range(N)]

q.append((0, start_r, start_c, 0))
visited[start_r][start_c][0b000000] = 0

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
answer = -1

while q:
    level, r, c, key = q.popleft()

    if maps[r][c] == '1':
        answer = level
        break

    for dr, dc in moves:
        if 0 <= r + dr < N and 0 <= c + dc < M:
            # 0. 출구인 경우
            if maps[r + dr][c + dc] == '1':
                q.appendleft((level + 1, r + dr, c + dc, key))
            # 1. 벽인 경우 -> 이동 불가
            elif maps[r + dr][c + dc] == '#': continue
            # 2. 열쇠인 경우 -> key 갱신 후 방문
            elif maps[r + dr][c + dc] in ['a', 'b', 'c', 'd', 'e', 'f']:
                new_key = key | (1 << (ord(maps[r + dr][c + dc]) - ord('a')))
                
                if visited[r + dr][c + dc][new_key] > level + 1:
                    visited[r + dr][c + dc][new_key] = level + 1
                    q.append((level + 1, r + dr, c + dc, new_key))
            # 3. 문인 경우 -> 해당 열쇠를 얻은 상태에서만 통과
            elif maps[r + dr][c + dc] in ['A', 'B', 'C', 'D', 'E', 'F']:
                if key & (1 << (ord(maps[r + dr][c + dc]) - ord('A'))):
                    if visited[r + dr][c + dc][key] > level + 1:
                        visited[r + dr][c + dc][key] = level + 1
                        q.append((level + 1, r + dr, c + dc, key))
            # 4. 빈 칸인 경우
            elif maps[r + dr][c + dc] == '.':
                if visited[r + dr][c + dc][key] > level + 1:
                    visited[r + dr][c + dc][key] = level + 1
                    q.append((level + 1, r + dr, c + dc, key))

print(answer)
