import sys

input = sys.stdin.readline

# 최대 20
N = int(input())
classroom = [[-1 for _ in range(N)] for _ in range(N)]
students = {}

# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

# 모든 학생에 대해서 반복 -> 20
# 모든 학생마다 모든 자리에 대해서 반복 -> 400
# 모든 자리에 대해서 인접한 방향에 대해서 반복 -> 4
# 자리 배치가 끝난 후 모든 학생에 대해서 인접한 방향 반복 -> 20 * 4 = 80
# 결론 -> 쌩 노가다로 때려박아서 구현해도 된단 말씀

# 인접한 4방향 이동을 위한 배열
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
# 자리 배치 후 만족도 계산을 위한 배열
satisfy = [0, 1, 10, 100, 1000]

for _ in range(N**2):
    student, *favor = map(int, input().rstrip().split())
    students[student] = favor

    # 앉을 수 있는 자리 후보
    seat_i, seat_j = N, N
    seat_favors = 0
    seat_emptys = 0

    # 모든 자리에 대해서 
    for i in range(N):
        for j in range(N):
            # 비어 있지 않은 자리라면 스킵
            if classroom[i][j] >= 0: continue

            favors = 0
            emptys = 0

            # 인접한 4개 방향에 대해서 조사
            for di, dj in moves:
                if 0 <= i + di < N and 0 <= j + dj < N:
                    if classroom[i + di][j + dj] in favor: favors += 1
                    elif classroom[i + di][j + dj] == -1: emptys += 1

            # print(i, j, favors, emptys)
            if seat_favors < favors:
                seat_i, seat_j, seat_favors, seat_emptys = i, j, favors, emptys
            elif seat_favors == favors and seat_emptys < emptys:
                seat_i, seat_j, seat_favors, seat_emptys = i, j, favors, emptys
            elif seat_favors == favors and seat_emptys == emptys and seat_i > i:
                seat_i, seat_j, seat_favors, seat_emptys = i, j, favors, emptys
            elif seat_favors == favors and seat_emptys == emptys and seat_i == i and seat_j > j:
                seat_i, seat_j, seat_favors, seat_emptys = i, j, favors, emptys

    classroom[seat_i][seat_j] = student

answer = 0

for i in range(N):
    for j in range(N):
        student = classroom[i][j]
        favor = students[student]

        cnt = 0

        for di, dj in moves:
            if 0 <= i + di < N and 0 <= j + dj < N:
                if classroom[i + di][j + dj] in favor:
                    cnt += 1

        answer += satisfy[cnt]

print(answer)
