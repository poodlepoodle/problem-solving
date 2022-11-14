import sys

def input(): return sys.stdin.readline().rstrip()

N, L = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

rows = []
# 가로 방향
for row in maps:
    rows.append(row)
# 세로 방향
for i in range(N):
    row = []
    for j in range(N):
        row.append(maps[j][i])
    rows.append(row)

# 두 개로 나누어 고려
# 1. 가다가 높이가 1개 낮아지는 경우
# 2. 가다가 높이가 1개 높아지는 경우

answer = 0

for row in rows:
    # print(row)
    available = True
    prev = row[0]
    visited = [False] * N

    for i in range(1, N):
        current = row[i]

        if prev == current:
            continue
        # 1. 가다가 높이가 1개 낮아지는 경우
        elif prev - 1 == current:
            # 경사로를 놓을 수 있을 만큼 L개의 블록이 다음에 연속되는지 확인
            count = 0
            # current부터 current + L - 1번째까지 검사
            for j in range(i, min(i + L, N)):
                if row[j] == current and not visited[j]:
                    count += 1
            if count >= L:
                for j in range(i, i + L):
                    visited[j] = True
            else:
                # print(f"{L} need but only counts {count} at current step {i}")
                available = False
                break
        # 2. 가다가 높이가 1개 높아지는 경우
        elif prev + 1 == current:
            # 경사로를 놓을 수 있을 만큼 L개의 블록이 이전에 연속됐는지 확인
            count = 0
            # prev - L부터 prev까지 검사
            for j in range(max(0, i - L), i):
                if row[j] == prev and not visited[j]:
                    count += 1
            if count >= L:
                for j in range(i - L, i):
                    visited[j] = True
            else:
                # print(f"{L} need but only counts {count} at current step {i}")
                available = False
        # 높이 차이가 1개보다 많은 경우는 제외
        else:
            available = False
            break

        prev = current

    if available:
        answer += 1

print(answer)
