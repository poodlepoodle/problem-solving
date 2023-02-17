import sys

input = sys.stdin.readline

# N은 최대 10^4
N, M = map(int, input().rstrip().split())

numbers = list(map(int, input().rstrip().split()))

# 모든 구간 i ~ j에 대해서 검사한다면... 10^4 * 10^4 = 10^8 -> 시간 초과
# 투 포인터로 O(N)에 처리 가능

left = 0
right = 0
temps = numbers[0]

answer = 0

while True:
    # print(numbers[left : right + 1], end=' ')

    if temps < M:
        if right < N - 1:
            right += 1
            temps += numbers[right]
        else: break
    else:
        if temps == M:
            answer += 1
        temps -= numbers[left]
        left += 1

    # print(answer)

print(answer)
