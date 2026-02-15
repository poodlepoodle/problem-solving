# 백준 16234번: 인구 이동 (2회차)

import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# N <= 50
# L, R <= 10^2
N, L, R = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 한 번의 인구 이동마다 모든 국가에 대해서 연합 조사
#   -> flood fill 방식으로 DFS 돌리면 될 듯...? -> O(N^2) ~= 10^3
# 인구 이동을 몇 번 해야 될 지는 모르겠으나, 모든 국가의 개수마다 한 번씩 하면 얼추 되지 않을까 예상
#   -> 10^3

moves = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
]

current_union = 0
stack = []
visited = None

def migrate(r, c):
    # print(f'dfs({r}, {c})')
    for dr, dc in moves:
        if 0 <= r + dr < N and 0 <= c + dc < N:
            if not visited[r + dr][c + dc]:
                if L <= abs(maps[r][c] - maps[r + dr][c + dc]) <= R:
                    global current_union
                    stack.append((r + dr, c + dc))
                    visited[r + dr][c + dc] = True
                    current_union += maps[r + dr][c + dc]
                    migrate(r + dr, c + dc)

answer = 0
while True:
    # print(f'* year: {answer}')
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            # 방문하지 않은 칸에 대해서 연합 조사
            if not visited[r][c]:
                cnt += 1

                # 연합 생성
                stack.append((r, c))
                visited[r][c] = True
                current_union += maps[r][c]
                migrate(r, c)

                # 생성된 연합에 대해서 인구 분배
                if len(stack) > 1:
                    # print('---------------')
                    # print(f'{cnt}번째 인구 이동')
                    num_humans = current_union // len(stack)
                    for sr, sc in stack:
                        maps[sr][sc] = num_humans
                    # for row in maps:
                    #     print(row)
                    # print('---------------')

                # 연합 해제 처리
                current_union = 0
                stack.clear()
    
    if cnt == N**2: break

    # for row in maps:
    #     print(row)
    # print()

    answer += 1

print(answer)
