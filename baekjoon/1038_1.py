from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input())

# N은 최대 10^6
# 대충 보면 N번째 감소하는 수는 N보다 크다는 점 때문에 O(N)을 고려하는 풀이는 의미가 없다

# 생각을 전환해서 가장 큰 감소하는 수를 생각해 보면...
# -> 9876543210(10자리 x 1개) ~ 0(1자리 x 10개) -> 최대 10^10 이하
decreasing_numbers = []
for k in range(1, 10 + 1):
    for numbers in combinations(range(0, 9 + 1), k):
        numbers = list(map(str, numbers))
        numbers.sort(reverse = True)
        decreasing_numbers.append("".join(numbers))

decreasing_numbers = list(map(int, decreasing_numbers))
decreasing_numbers.sort()

print(decreasing_numbers[N] if N < len(decreasing_numbers) else -1)
