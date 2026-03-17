# 백준 2470번: 두 용액

import sys

input = sys.stdin.readline

# N <= 10^5
N = int(input())
# -10^9 <= fluids[i] <= 10^9
fluids = list(map(int, input().rstrip().split()))
fluids.sort()
# print(fluids)

# 브루트포싱 -> O(N^2) => 10^10, TLE 예상
# 접근 -> 정렬 및 Two Pointer -> O(2N), AC 예상

left, right = 0, N - 1
sums = fluids[left] + fluids[right]
answer = [fluids[left], fluids[right]]
answer_sums = sum(answer)

while left < right:
    # print(fluids[left], fluids[right], sums)

    if abs(sums) < abs(answer_sums):
        answer_sums = sums
        answer = [fluids[left], fluids[right]]

    if sums < 0:
        sums -= fluids[left]
        left += 1
        sums += fluids[left]
    elif sums > 0:
        sums -= fluids[right]
        right -= 1
        sums += fluids[right]
    else:
        break

print(*answer)
