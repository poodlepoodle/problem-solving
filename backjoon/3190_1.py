from collections import deque
import sys

input = sys.stdin.readline

# 보드의 크기 N
# 0은 빈 칸, 1은 벽, 2는 사과, 3은 뱀
N = int(input())
board = [[1 for _ in range(N + 2)] for _ in range(N + 2)]
for i in range(N):
    for j in range(N):
        board[i + 1][j + 1] = 0

# 사과의 갯수 K
for _ in range(int(input())):
    r, c = map(int, input().rstrip().split())
    board[r][c] = 2

# 뱀의 방향 변환 횟수 L
rotations = deque()
for _ in range(int(input())):
    times, direction = input().rstrip().split()
    rotations.append((int(times), direction))

# 순서대로 오른쪽 - 아래 - 왼쪽 - 윗쪽
moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 뱀의 초기 위치 : 1행 1열
snake = deque([(1, 1)])
head_r, head_c = 1, 1
board[head_r][head_c] = 3
# 뱀의 초기 방향 : 오른쪽
snake_direction = 0

# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
seconds = 0
while True:
    seconds += 1
    # print(f"{seconds}초")
    # print(snake)
    # for row in board:
    #     print(row)
    # print()

    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    dr, dc = moves[snake_direction]
    head_r, head_c = head_r + dr, head_c + dc
    snake.append((head_r, head_c))

    # 만약 이동한 칸이 벽이거나 뱀이라면,
    if board[head_r][head_c] == 1 or board[head_r][head_c] == 3:
        break
    # 만약 이동한 칸에 사과가 있다면,
    elif board[head_r][head_c] == 2:
        # 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        board[head_r][head_c] = 3
    # 만약 이동한 칸에 사과가 없다면,
    else:
        board[head_r][head_c] = 3
        # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        tail_r, tail_c = snake.popleft()
        board[tail_r][tail_c] = 0

    # 방향 전환을 해야 하는 경우
    if rotations and rotations[0][0] <= seconds:
        _, C = rotations.popleft()
        # print("회전 : ", end = "")

        if C == 'L':
            # print("왼쪽")
            snake_direction = (snake_direction + 3) % 4
        elif C == 'D':
            # print("오른쪽")
            snake_direction = (snake_direction + 1) % 4

print(seconds)
