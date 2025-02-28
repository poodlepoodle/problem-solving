# 백준 1806번: 부분합

import sys

input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
# print(numbers)

prefixes = [0]
for num in numbers: # 10^5
    prefixes.append(prefixes[-1] + num)
# print(prefixes)

i, j = 0, 1
answer = 100001

while i < j:
    current_sum = prefixes[j] - prefixes[i]
    # print(i, j, current_sum)

    if current_sum >= S:
        answer = min(answer, j - i)
        # print('!')
        if i + 1 < j:
            i += 1
        elif j < N:
            j += 1
        else:
            break
    elif j < N:
        j += 1
    else:
        i += 1

print(answer if answer != 100001 else 0)
