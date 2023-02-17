import sys

input = sys.stdin.readline

# N, M <= 50
N, M = map(int, input().rstrip().split())

board = [list(input().rstrip()) for _ in range(N)]

# 생각나는 방법 두 개
# 1. 바로 이전 칸을 제외하고, 방문한 적 있는 칸이라면 YES
# 2. 현재 탐색 횟수가 3번 이상이고, 방문한 적 있는 칸이라면 YES

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

def dfs(r, c, level, letter):
    # print(f"({r}, {c})")
    answer = False

    for dr, dc in moves:
        if (0 <= r + dr < N) and (0 <= c + dc < M) and (board[r + dr][c + dc] == letter):
            if visited[r + dr][c + dc]:
                if level - visited[r + dr][c + dc] >= 3:
                    return True
            else:
                visited[r + dr][c + dc] = level + 1
                answer = answer or dfs(r + dr, c + dc, level + 1, letter)

    return answer

visited = [[False for _ in range(M)] for _ in range(N)]
answer = False

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            visited[i][j] = 1
            answer = answer or dfs(i, j, 1, board[i][j])
        if answer: break
    if answer: break

print('Yes' if answer else 'No')
