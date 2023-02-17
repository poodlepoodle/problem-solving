import sys

input = sys.stdin.readline

# T <= 10^3, W <= 30
T, W = map(int, input().rstrip().split())

# 0
# 1
# 2
# 2
# 2

jadoos = []

tree = 1
cnt = 0

for _ in range(T): # 10^3
    current = int(input())
    # print(current, cnt)

    if current == tree:
        cnt += 1
    else:
        jadoos.append(cnt)
        cnt = 1
        tree = current

jadoos.append(cnt)

while len(jadoos) < W + 1:
    jadoos.append(0)

print(jadoos)

# 위에서 구한 jadoos 배열에서 W + 1개 만큼 연속된 요소를 선택해 최대 합을 산출
answer = 0
for idx in range(len(jadoos) - W):
    answer = max(answer, sum(jadoos[idx : idx + W + 1]))

print(answer)
