import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

r, c, direction = map(int, input().split())

# 북 - 동 - 남 - 서
view_directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

# 빈 칸은 0, 벽은 1, 청소한 칸은 2
maps = [list(map(int, input().split())) for _ in range(N)]

answer = 0

while True:
    cleaned = False

    # 현재 위치를 청소한다.
    if maps[r][c] == 0:
        maps[r][c] = 2
        answer += 1

    # 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
    for i in range(4):
        dr, dc = view_directions[(direction + 3 - i) % 4]

        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
        if maps[r + dr][c + dc] == 0:
            # 그 방향으로 회전한 다음
            direction = (direction + 3 - i) % 4
            # 한 칸을 전진하고
            r, c = r + dr, c + dc
            # 1번부터 진행한다.
            cleaned = True
            break
        # 왼쪽 방향에 청소할 공간이 없다면,
        else:
            # 그 방향으로 회전하고 2번으로 돌아간다.
            pass

    # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는,
    if not cleaned:
        # 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는
        dr, dc = view_directions[(direction + 2) % 4]
        if maps[r + dr][c + dc] == 1:
            # 작동을 멈춘다.
            break
        # 그렇지 않은 경우,
        else:
            # 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            r, c = r + dr, c + dc

print(answer)
