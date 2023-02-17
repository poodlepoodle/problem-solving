from collections import deque
import sys

input = sys.stdin.readline

# N은 최대 10^3
N = int(input())

in_orders = [input().rstrip() for _ in range(N)]
out_orders = deque([input().rstrip() for _ in range(N)])

# print(in_orders)
# print(out_orders)

# 뭔가 무조건 그리디의 느낌이 난다...

# 1 2 3 4 5 6
# 4 1 5 2 3 6

answer = 0
idx = 0

while out_orders:
    # 방금 터널에서 나온 차의 번호
    car = out_orders.popleft()
    # print(car)

    # 순서에 맞게 차가 나온 경우
    if car == in_orders[idx]:
        idx += 1
    else:
        answer += 1
        in_orders.remove(car)

print(answer)
