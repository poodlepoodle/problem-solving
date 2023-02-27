import sys

input = sys.stdin.readline

# R, C <= 10^2, M <= 10^4
R, C, M = map(int, input().rstrip().split())
pool = [[0 for _ in range(C)] for _ in range(R)]

moves = ((-1, 0), (1, 0), (0, 1), (0, -1))
opposites = (1, 0, 3, 2)

sharks = {}
sharks_num = 1
for _ in range(M):
    # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
    r, c, s, d, z = map(int, input().rstrip().split())

    sharks[sharks_num] = (r - 1, c - 1, s, d - 1, z)
    pool[r - 1][c - 1] = sharks_num

    sharks_num += 1

# print('pool 2차원 공간: ')
# for row in pool:
#     for letter in row:
#         print(letter, end=' ')
#     print()
# print()

# import pprint
# print('sharks 딕셔너리: ')
# pprint.pprint(sharks)

# 낚시왕이 모든 열을 방문 -> 10^2
# 각 열마다 상어를 탐색 -> 10^2
# 각 초마다 상어들의 움직임 계산 -> 10^4
# 결론: 상어가 꽉꽉 차있다고 해도 10^4마리보다 훨씬 줄어들어 갈 것이므로 10^8 내에 통과한다고 봄
# 뿐만 아니라, 낚시왕이 각 열의 모든 행을 탐색할 경우는 실질적으로 없을 것이므로...

answer = 0

for c in range(C):
    # 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
    # print(c)

    # 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
    for r in range(R):
        # 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
        if pool[r][c]:
            answer += sharks[pool[r][c]][4]
            sharks.pop(pool[r][c])
            pool[r][c] = False
            break

    # 3. 상어가 이동한다.
    for r in range(R):
        for c in range(C):
            pool[r][c] = False

    next_sharks = []
    for key in sharks.keys():
        r, c, speed, direction, size = sharks[key]

        # 원래 상어의 위치를 제거
        pool[r][c] = False
        next_r, next_c = r, c

        # 0 = 10 = 20 = 30 = ...
        # 0, 1, 2, 3, 4, 5, 4, 3, 2, 1

        if direction == 0 or direction == 1:
            speed = speed % ((R - 1) * 2)
        else:
            speed = speed % ((C - 1) * 2)

        for _ in range(speed):
            dr, dc = moves[direction]
            next_r = next_r + dr
            next_c = next_c + dc

            if not (0 <= next_r < R and 0 <= next_c < C):
                direction = opposites[direction]

                dr, dc = moves[direction]
                next_r += dr * 2
                next_c += dc * 2

        sharks[key] = next_r, next_c, speed, direction, size
        next_sharks.append((next_r, next_c, key))

    for r, c, shark_num in next_sharks:
        if not pool[r][c]:
            pool[r][c] = shark_num
        else:
            # 이동이 끝난 후 각 칸에는 가장 크기가 큰 상어 한 마리만 들어감
            if sharks[pool[r][c]][4] < sharks[shark_num][4]:
                sharks.pop(pool[r][c])
                pool[r][c] = shark_num
            else:
                sharks.pop(shark_num)

    # for row in pool:
    #     for letter in row:
    #         print(letter if letter else '_', end=' ')
    #     print()
    # print()

print(answer)
