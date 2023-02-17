import sys

input = sys.stdin.readline

# 최대 10^1
T = int(input())

for _ in range(T):
    N = int(input())

    # 최대 10^5
    numbers = list(map(int, input().rstrip().split()))

    # prefix sum ->
    # sum 배열을 계산하는 데 10^5
    # 모든 경우의 수를 구하는 데 10^10 -> 불가능

    # two pointer ->
    # 2 * 10^5 -> 이거 맞나??
    left, right = 0, 1
    max_xor = 0
    xor = numbers[0]

    if N == 1:
        print(numbers[0])
        continue

    while right < N:
        print(left, right)
        if left == right or xor > xor ^ numbers[right + 1]:
            xor ^= numbers[right + 1]
            right += 1
        else:
            xor ^= numbers[left]
            left += 1

    print()