# 백준 10775번: 공항

import sys

input = sys.stdin.readline

# 게이트의 개수 G <= 10^5
G = int(input())

# 비행기의 개수 P <= 10^5
P = int(input())

# 문제 풀이 전략
# 1. 1번 ~ Gi번 게이트까지 도킹할 수 있는 비행기는 Gi번 게이트의 도킹 여부를 검사함
# 2. 만약 도킹 가능하다면, 바로 도킹함
# 3. 만약 도킹 불가능하다면, Gi번 게이트가 가리키는 부모 게이트에 도킹 가능함
# 4. 만약 Gi번 게이트의 부모 게이트가 0인 경우, 더 이상 도킹할 수 있는 게이트가 없을 것이므로 종료

parent_gate = [i for i in range(G + 1)]
# print(parent_gate)

def find(x):
    if x == parent_gate[x]: return x
    parent_gate[x] = find(parent_gate[x])
    return parent_gate[x]

def union(A, B):
    # print(f"union({A}, {B})")
    find_A = find(A)
    find_B = find(B)

    if find_A < find_B:
        parent_gate[find_B] = find_A
    elif find_A > find_B:
        parent_gate[find_A] = find_B

answer = 0

for _ in range(P):
    Gi = int(input())

    if find(Gi):
        union(find(Gi), find(Gi) - 1)
    else:
        break

    # print(Gi, parent_gate)
    answer += 1

print(answer)
