import sys

input = sys.stdin.readline

# N은 최대 10^6, M은 최대 10^5
N, M = map(int, input().rstrip().split())

groups = list(range(0, N + 1))

def find(a):
    A = a

    while groups[A] != A:
        A = groups[A]

    groups[a] = A
    return A

for _ in range(M):
    opcode, a, b = map(int, input().rstrip().split())

    A = find(a)
    B = find(b)

    # 합집합 연산
    if opcode == 0:
        if A != B:
            if A < B:
                groups[B] = A
            else:
                groups[A] = B
        
    # 같은 집합 원소 확인
    elif opcode == 1:
        if A == B: print('YES')
        else: print('NO')
