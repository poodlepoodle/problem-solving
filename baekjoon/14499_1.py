import sys

input = sys.stdin.readline

# 지도의 세로 크기 N, 가로 크기 M, 주사위를 놓은 곳의 좌표 x, y, 명령의 개수 K
# 명령의 개수 K는 최대 10^3
N, M, R, C, K = map(int, input().rstrip().split())

maps = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 순서대로 윗면, 뒷면, 오른쪽, 왼쪽, 앞면, 아랫면
dices = [0, 0, 0, 0, 0, 0]

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
for command in list(map(int, input().rstrip().split())):
    if command == 1:
        if C == M - 1: continue
        C += 1

        dices[0], dices[2], dices[3], dices[5] = dices[2], dices[5], dices[0], dices[3]

    elif command == 2:
        if C == 0: continue
        C -= 1

        dices[0], dices[2], dices[3], dices[5] = dices[3], dices[0], dices[5], dices[2]
    
    elif command == 3:
        if R == 0: continue
        R -= 1

        dices[0], dices[1], dices[4], dices[5] = dices[1], dices[5], dices[0], dices[4]

    elif command == 4:
        if R == N - 1: continue
        R += 1

        dices[0], dices[1], dices[4], dices[5] = dices[4], dices[0], dices[5], dices[1]

    # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면,
    if maps[R][C] == 0:
        # 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
        maps[R][C] = dices[5]
    # 0이 아닌 경우에는
    else:
        # 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
        dices[5], maps[R][C] = maps[R][C], 0

    print(dices[0])
