# 백준 17143번: 낚시왕 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# R, C <= 10^2
R, C, M = map(int, input().rstrip().split())
maps = [[0 for _ in range(C)] for _ in range(R)]

sharks = {}
for _ in range(M):
    r, c, speed, direction, size = map(int, input().rstrip().split())
    maps[r - 1][c - 1] = size
    if direction in [1, 2]:
        sharks[size] = (direction, speed % (2 * (R - 1)))
    else:
        sharks[size] = (direction, speed % (2 * (C - 1)))

moves = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, 1],
    4: [0, -1]
}

opposite = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

# 시간복잡도 계산
# 1. 낚시왕이 오른쪽으로 한 칸 이동 -> O(1)
# 2. 열에서 가장 가까운 상어를 잡음 -> O(R) = 10^2
# 3. 모든 상어가 이동함 -> O(RC) * O(10^3) = 10^7
# 4. 1~3의 과정을 낚시왕이 모든 열만큼 반복 -> O(C) = 10^2
# 결론: 그냥은 통과 못 할것 같고, 상어의 이동 시 속력을 나누어 이동하지 않고 바로 처리해 버리면 가능할듯?
#   - 예시로 한 번 방향과 칸을 제자리로 돌아오는 만큼은 MOD를 취해도 된다던지... (2R or 2C)
# 요구사항 구현
# 1. 상어는 각각 유니크한 크기를 가지므로, 해시맵으로 관리해도 좋을 듯
# 2. 각 상어의 이동 사이에는 공간을 비워 주고, 잠시 큐에 넣어서 다시 재분배하는 방식으로 구현하면 자연스러울듯

def print_board():
    for r in range(R):
        for c in range(C):
            if not maps[r][c]: print('.', end=' ')
            else: print(maps[r][c], end=' ')
        print()

def is_in_board(r, c):
    return 0 <= r < R and 0 <= c < C

def sharks_move():
    q = deque()

    for r in range(R):
        for c in range(C):
            if maps[r][c]:
                q.append((r, c, maps[r][c]))
                maps[r][c] = 0

    while q:
        r, c, size = q.popleft()
        direction, speed = sharks[size]
        dr, dc = moves[direction]

        for _ in range(speed):
            new_r, new_c = r + dr, c + dc
            if not is_in_board(new_r, new_c):
                direction = opposite[direction]
                dr, dc = moves[direction]
                new_r, new_c = r + dr, c + dc

            r, c = new_r, new_c

        # 더 큰 상어가 이미 위치해 있는 경우
        if maps[r][c] and maps[r][c] > size:
            del sharks[size]
            continue

        maps[r][c] = size
        sharks[size] = (direction, speed)

fisher_c = -1
answer = 0

# print_board()
# print()

while fisher_c < C - 1:
    # 낚시왕이 오른쪽으로 한 칸 이동
    fisher_c += 1
    # print(f'fisher is in column {fisher_c}')

    # 열에서 가장 가까운 상어를 잡음
    for r in range(R):
        if maps[r][fisher_c]:
            del sharks[maps[r][fisher_c]]
            answer += maps[r][fisher_c]
            maps[r][fisher_c] = 0
            break

    # 모든 상어가 이동함
    sharks_move()

    # print_board()
    # print(f'answer: {answer}')
    # print()

print(answer)
