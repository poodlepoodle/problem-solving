# 백준 21608번: 상어 초등학교 (2회차)

import sys

input = sys.stdin.readline

# N <= 20
N = int(input())

maps = [[0 for _ in range(N)] for _ in range(N)]
# for row in maps:
#     print(row)
# print()

moves = ((-1, 0), (1, 0), (0, -1), (0, 1))
students = {}

for _ in range(N ** 2):
    student, *favors = map(int, input().rstrip().split())
    students[student] = favors
    # print(student, favors)

    # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    max_cnt = -1
    candidates = []
    
    for r in range(N):
        for c in range(N):
            # 이미 학생이 위치한 자리는 패스
            if maps[r][c] > 0: continue

            cnt = 0
            for dr, dc in moves:
                if 0 <= r + dr < N and 0 <= c + dc < N:
                    # 좋아하는 학생이 인접한 칸에 앉아있다면
                    if maps[r + dr][c + dc] and maps[r + dr][c + dc] in favors:
                        cnt += 1

            if cnt >= max_cnt:
                if cnt > max_cnt:
                    max_cnt = cnt
                    candidates.clear()
                candidates.append((r, c))

    # print(f"candidates: {candidates}")
    if len(candidates) == 1:
        r, c = candidates[0]
        maps[r][c] = student
        # for row in maps:
        #     print(row)
        # print()
        continue

    # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    max_cnt = -1
    next_candidates = []

    for r, c in candidates:
        cnt = 0

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if not maps[r + dr][c + dc]: cnt += 1
        
        if cnt >= max_cnt:
            if cnt > max_cnt:
                max_cnt = cnt
                next_candidates.clear()
            next_candidates.append((r, c))

    # print(f"next_candidates: {next_candidates}")

    r, c = next_candidates[0]
    maps[r][c] = student

    # for row in maps:
    #     print(row)
    # print()

answer = 0

for r in range(N):
    for c in range(N):
        student = maps[r][c]
        favors = students[student]

        cnt = 0

        for dr, dc in moves:
            if 0 <= r + dr < N and 0 <= c + dc < N:
                if maps[r + dr][c + dc] in favors:
                    cnt += 1

        if cnt == 4: answer += 1000
        elif cnt == 3: answer += 100
        elif cnt == 2: answer += 10
        elif cnt == 1: answer += 1

print(answer)
