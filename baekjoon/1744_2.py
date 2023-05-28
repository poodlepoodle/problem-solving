# 백준 1744번: 수 묶기 (2회차)

import sys

input = sys.stdin.readline

# N <= 50
N = int(input())

numbers = [int(input()) for _ in range(N)]

# 1. 수는 그냥 더해지는 것보다 묶는 게 왠만하면 이득
# 2. 음수는 음수끼리, 양수는 양수끼리 묶어야 이득
# 3. 0은 더해 봐야 본전, 묶으면 손해, 단, 음수가 1개 남았을 경우엔 곱하면 이득
# 4. 양수 1은 묶는 것보다 더하는 게 무조건 이득

left = [-number for number in numbers if number < 0]
right = [number for number in numbers if number > 1]
ones = [number for number in numbers if number == 1]
len_zeros = numbers.count(0)

left.sort()
right.sort()

# print(left)
# print(ones)
# print(right)

answer = 0

while len(left) >= 2:
    answer += (left.pop() * left.pop())
if left and len_zeros == 0: answer -= left.pop()

while len(right) >= 2:
    answer += (right.pop() * right.pop())
if right: answer += right.pop()

answer += sum(ones)

print(answer)
