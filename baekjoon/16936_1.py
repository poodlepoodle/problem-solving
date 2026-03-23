# 백준 16936번: 나3곱2

from collections import defaultdict
import sys

input = sys.stdin.readline

# N <= 10^2
N = int(input())
# 1 <= B[i] <= 10^18
B = list(map(int, input().rstrip().split()))
B.sort() # < 10^4
# print(B)

# 정리
#   - 특정 수 X가 존재, 단 수열 B중에서 어떤 게 X인지는 모름
#   - 나3은 3으로 나누기, 곱2는 2를 곱하기
# 접근
#   - 각 수마다의 그래프처럼 고려한다면?

graph = defaultdict(list)
for i in range(len(B)): # 10^4
    for j in range(i + 1, len(B)):
        a, b = B[i], B[j]
        if a * 3 == b:
            graph[b].append(a)
        elif a * 2 == b:
            graph[a].append(b)
# print(graph)

stack = []
def dfs(current, depth):
    # print(f'dfs({current}, {depth})')

    if depth >= N:
        if len(stack) == N: return True
        return False
    
    for next in graph[current]:
        stack.append(next)
        return dfs(next, depth + 1)

for start in B:
    stack.clear()
    stack.append(start)
    if dfs(start, 1): break
    # print(stack)
    # print()

print(*stack)
