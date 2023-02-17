import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

belts = list(map(int, input().rstrip().split()))
robots = [False] * N

answer = 1
# print(0)
# print(belts)
# print(robots)
# print()

# 컨베이어 벨트를 이용해 로봇들을 건너편으로 옮기려고 한다.
# 로봇을 옮기는 과정에서는 아래와 같은 일이 순서대로 일어난다.
while True:
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belts = belts[-1:] + belts[:-1]
    # 로봇이 있는 칸의 인덱스 : 0 ~ N-1
    robots = robots[-1:] + robots[:-1]

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며,
    # 그 칸의 내구도가 1 이상 남아 있어야 한다.
    robots[N - 1] = False
    for idx in range(N - 2, -1, -1):
        if robots[idx] and not robots[idx + 1] and belts[idx + 1] > 0:
            robots[idx + 1], robots[idx] = True, False
            belts[idx + 1] -= 1
    robots[N - 1] = False
    # 만약 이동할 수 없다면 가만히 있는다.

    if not robots[0] and belts[0] > 0:
        robots[0] = True
        belts[0] -= 1

    # print(answer)
    # print(belts)
    # print(robots)
    # print()

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if len([belt for belt in belts if belt == 0]) >= K:
        break

    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    answer += 1

print(answer)
