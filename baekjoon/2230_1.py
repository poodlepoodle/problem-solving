# 백준 2230번: 수 고르기

import sys

input = sys.stdin.readline

# N <= 10^5
N, M = map(int, input().rstrip().split())
# 0 <= numbers[i] <= 10^9
numbers = [int(input()) for _ in range(N)]
numbers.sort()

# 포인트
#   - 수열은 정렬 및 재배열 가능
#   - Two Pointer로 풀자!

left, right = 0, 1
answer = 2 * int(1e9) + 1
while right < N:
    # print(left, right)
    if left == right: right += 1
    elif numbers[right] - numbers[left] >= M:
        answer = min(answer, numbers[right] - numbers[left])
        left += 1
    else:
        right += 1
    # print()

print(answer)
