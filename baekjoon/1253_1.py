# 백준 1253번: 좋다

from collections import defaultdict
import sys

input = sys.stdin.readline

# N <= 2 * 10^3
N = int(input())

numbers = list(map(int, input().rstrip().split()))
numbers.sort()
# print(numbers)

is_good = defaultdict(bool)

def search(target):
    left, right = 0, N - 1
    
    while left <= right:
        middle = (left + right) // 2

        if target == numbers[middle]:
            return middle
        elif target < numbers[middle]:
            right = middle - 1
        else:
            left = middle + 1
    
    return -1

for idx_A in range(N):
    A = numbers[idx_A]

    for idx_B in range(N):
        if idx_A == idx_B: continue

        B = numbers[idx_B]
        C = A + B

        idx_C = search(C)
        if idx_C != -1:
            if idx_C != idx_A and idx_C != idx_B:
                # print(A, '+', B, '=', C)
                is_good[C] = True
    #             print(f'{C} is good')
    # print()

answer = 0
# print(numbers)
for number in numbers:
    # print(number)
    if is_good[number]:
        answer += 1
print(answer)
