import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())

board = [list(input().rstrip()) for _ in range(R)]

moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

def dfs(r, c, visited, level):
    global answer
    answer = max(answer, level)

    for dr, dc in moves:
        if 0 <= r + dr < R and 0 <= c + dc < C:
            if not (visited & (1 << (ord(board[r + dr][c + dc]) - ord('A')))):
                dfs(r + dr, c + dc, visited ^ (1 << (ord(board[r + dr][c + dc]) - ord('A'))), level + 1)

answer = -1
dfs(0, 0, 1 << (ord(board[0][0]) - ord('A')), 1)
print(answer)
