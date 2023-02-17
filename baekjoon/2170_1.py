import sys

input = sys.stdin.readline

# 최대 10^6
N = int(input())
lines = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
lines.sort(key=lambda x:(x[0], x[1]))

left = lines[0][0]
right = lines[0][1]
emptys = 0

for x1, x2 in lines[1:]:
    if x1 > right:
        emptys += (x1 - right)

    right = max(right, x2)

    # print(left, right)

# 정답 출력
print((right - left) - emptys)
