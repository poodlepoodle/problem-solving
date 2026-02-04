# 백준 20055번: 컨베이어 벨트 위의 로봇 (2회차)

import sys

input = sys.stdin.readline

# 컨베이어 벨트의 길이 N <= 10^2
N, K = map(int, input().rstrip().split())
len_total_belts = 2 * N

EMPTY_BELT = '_'

hps = list(map(int, input().rstrip().split()))
hp_zeros = len([hp for hp in hps if hp == 0])
belts = [EMPTY_BELT for _ in hps]
robot_idx = 1
# print('belts:', *belts)
# print('hps:', hps)
# print()

def is_robot_avaliable_to_move(idx):
    return idx + 1 <= N - 1 and hps[idx + 1] > 0 and belts[idx + 1] == EMPTY_BELT

answer = 1
while True:
    # 1. 벨트가 한 칸씩 로봇과 함께 회전
    # print(' * 벨트가 한 칸씩 로봇과 함께 회전')
    hps = hps[-1:] + hps[:-1]
    belts = belts[-1:] + belts[:-1]
    # print('belts:', *belts)
    # print('hps:', hps)

    # 2. 가장 먼저 올라간 로봇부터 이동 가능 판단하고 이동
    # print(' * 가장 먼저 올라간 로봇부터 이동 가능 판단하고 이동')
    for idx in range(N - 1, -1, -1):
        if belts[idx] == EMPTY_BELT: continue

        if idx == N - 1:
            belts[idx] = EMPTY_BELT
        if is_robot_avaliable_to_move(idx):
            hps[idx + 1] -= 1
            if hps[idx + 1] == 0: hp_zeros += 1
            belts[idx], belts[idx + 1] = EMPTY_BELT, belts[idx]
        # 도착점에서 제거
        if idx + 1 == N - 1:
            belts[idx + 1] = EMPTY_BELT
    # print('belts:', *belts)
    # print('hps:', hps)

    # 3. 올리는 위치의 내구도가 0이 아니면 로봇 추가
    # print(' * 올리는 위치의 내구도가 0이 아니면 로봇 추가')
    if hps[0] > 0:
        belts[0] = robot_idx
        robot_idx += 1

        hps[0] -= 1
        if hps[0] <= 0: hp_zeros += 1
    # print('belts:', *belts)
    # print('hps:', hps)
    
    # 내구도가 0인 칸의 개수가 K 이상이면 종료
    if hp_zeros >= K:
        break

    answer += 1
    # print('-------------\n', answer)
    # print('belts:', *belts)
    # print('hps:', hps)
    # print()

print(answer)
