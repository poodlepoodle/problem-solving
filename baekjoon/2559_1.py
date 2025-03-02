# 백준 2559번: 수열

import sys

input = sys.stdin.readline

# N, K <= 10^5
N, K = map(int, input().rstrip().split())

hots = list(map(int, input().rstrip().split()))

left = 0
right = K - 1
temp_sum = sum(hots[:right + 1]) 

answer = temp_sum

while right < N - 1:
    temp_sum -= hots[left]
    left, right = left + 1, right + 1
    temp_sum += hots[right]

    if temp_sum > answer: answer = temp_sum

print(answer)
