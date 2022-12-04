from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]

# 컨셉 : 흔한 미로 탈출 BFS ("불!" 과 유사한 문제)
# 그러나... 특정 열쇠를 얻은 후에 이미 방문한 칸의 방문 여부를 초기화하고 다시 방문할 수 있음

# visited = [[[1e9 for _ in range(2**6)] for _ in range(M)] for _ in range(N)]
visited = [[[1e9 for _ in range(M)] for _ in range(N)] for _ in range(2**6)]
q = deque()

for i in range(N):
    for j in range(M):
        if maze[i][j] == '0':
            maze[i][j] = '.'
            q.append((0, i, j, 0))
            visited[0][i][j] = 0

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
answer = -1

# 빈 칸: 언제나 이동할 수 있다. ('.')
# 벽: 절대 이동할 수 없다. ('#')
# 열쇠: 언제나 이동할 수 있다. 이 곳에 처음 들어가면 열쇠를 집는다. ('a', 'b', 'c', 'd', 'e', 'f')
# 문: 대응하는 열쇠가 있을 때만 이동할 수 있다. ('A', 'B', 'C', 'D', 'E', 'F')
# 민식이의 현재 위치: 빈 곳이고, 민식이가 현재 서 있는 곳이다. ('0')
# 출구: 달이 차오르기 때문에, 민식이가 가야하는 곳이다. 이 곳에 오면 미로를 탈출한다. ('1')

while q:
    level, r, c, key = q.popleft()
    # print(level, f"({r}, {c})", bin(key)[2:].zfill(6))

    for dr, dc in moves:
        # 좌표를 벗어나는 경우 제외
        if not (0 <= r + dr < N and 0 <= c + dc < M): continue
        # 벽
        elif maze[r + dr][c + dc] == '#': continue
        # 방문이 최소 거리가 아닌 경우
        elif level + 1 >= visited[key][r + dr][c + dc]: continue
        # 출구
        elif maze[r + dr][c + dc] == '1':
            answer = level + 1
            break

        # 빈 칸
        if maze[r + dr][c + dc] == '.':
            q.append((level + 1, r + dr, c + dc, key))
            visited[key][r + dr][c + dc] = level + 1
        # 문
        elif maze[r + dr][c + dc] in ('A', 'B', 'C', 'D', 'E', 'F'):
            if key & (1 << (ord(maze[r + dr][c + dc]) - ord('A'))):
                q.append((level + 1, r + dr, c + dc, key))
                visited[key][r + dr][c + dc] = level + 1
        # 열쇠
        elif maze[r + dr][c + dc] in ('a', 'b', 'c', 'd', 'e', 'f'):
            new_key = key | (1 << (ord(maze[r + dr][c + dc]) - ord('a')))
            if visited[new_key][r + dr][c + dc] > level + 1:
                q.append((level + 1, r + dr, c + dc, new_key))
                visited[new_key][r + dr][c + dc] = level + 1
    
    if answer != -1: break

print(answer)
