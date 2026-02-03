# 백준 1717번: 집합의 표현 (2회차)

import sys

input = sys.stdin.readline

# N <= 10^6
# M <= 10^5
N, M = map(int, input().rstrip().split())

parents = [i for i in range(N + 1)]
# print(parents[1:])
# print()

def find(x):
    current = x
    while current != parents[current]:
        current = parents[current]
    parents[x] = current
    return parents[x]

def union(A, B):
    parent_A, parent_B = find(A), find(B)

    if parent_A <= parent_B:
        parents[parent_B] = parent_A
    else:
        parents[parent_A] = parent_B

for _ in range(M):
    command, A, B = map(int, input().rstrip().split())
    # print('union' if command == 0 else 'check', A, 'between', B)

    if command == 0 and A != B:
        union(A, B)
    elif command == 1:
        if A == B: print('YES')
        else: print('YES' if find(A) == find(B) else 'NO')

    # print(parents[1:])
    # print()
