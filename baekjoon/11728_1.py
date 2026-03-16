# 백준 11728번: 배열 합치기

import sys

input = sys.stdin.readline

# N, M <= 10^6
N, M = map(int, input().rstrip().split())

# A, B는 정렬되어 있음
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))

ptr_A, ptr_B = 0, 0
answer = []

while ptr_A < N and ptr_B < M:
    if A[ptr_A] <= B[ptr_B]:
        answer.append(A[ptr_A])
        ptr_A += 1
    else:
        answer.append(B[ptr_B])
        ptr_B += 1

while ptr_A < N:
    answer.append(A[ptr_A])
    ptr_A += 1
while ptr_B < M:
    answer.append(B[ptr_B])
    ptr_B += 1

print(*answer)
