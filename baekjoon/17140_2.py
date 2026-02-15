# 백준 17140번: 이차원 배열과 연산 (2회차)

import sys

input = sys.stdin.readline

MAX_LENGTH = 100

# R, C, K <= 10^2
R, C, K = map(int, input().rstrip().split())
A = [[0 for _ in range(MAX_LENGTH)] for _ in range(MAX_LENGTH)]

array = [list(map(int, input().rstrip().split())) for _ in range(3)]
for r in range(3):
    for c in range(3):
        A[r][c] = array[r][c]

len_R, len_C = 3, 3

second = 0
while True:
    if A[R - 1][C - 1] == K: break
    if second >= 100:
        second = -1
        break

    # R연산
    if len_R >= len_C:
        new_len_C = 0
        for r in range(len_R): # 10^2
            counter = {}

            for c in range(0, len_C): # 10^2
                counter[A[r][c]] = counter.get(A[r][c], 0) + 1
            new_row = [[key, value] for key, value in counter.items()]
            new_row.sort(key=lambda x:(x[1], x[0]))
            new_numbers = []
            for n1, n2 in new_row:
                if n1 > 0:
                    new_numbers.append(n1)
                    new_numbers.append(n2)

            for c in range(len(new_numbers)):
                A[r][c] = new_numbers[c]
            new_len_C = max(new_len_C, len(new_numbers))
            for c in range(len(new_numbers), max(new_len_C, len_C)):
                A[r][c] = 0
            
        len_C = max(len_C, new_len_C)
    # C연산
    else:
        new_len_R = 0
        for c in range(len_C): # 10^2
            counter = {}

            for r in range(0, len_R): # 10^2
                counter[A[r][c]] = counter.get(A[r][c], 0) + 1
            new_row = [[key, value] for key, value in counter.items()]
            new_row.sort(key=lambda x:(x[1], x[0]))
            new_numbers = []
            for n1, n2 in new_row:
                if n1 > 0:
                    new_numbers.append(n1)
                    new_numbers.append(n2)

            for r in range(len(new_numbers)):
                A[r][c] = new_numbers[r]
            new_len_R = max(new_len_R, len(new_numbers))
            for r in range(len(new_numbers), max(new_len_R, len_R)):
                A[r][c] = 0
            
        len_R = max(len_R, new_len_R)

    # for r in range(len_R):
    #     for c in range(len_C):
    #         print(A[r][c], end='')
    #     print()
    # print()

    second += 1

print(second)
