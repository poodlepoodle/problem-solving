import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
groups = [i for i in range(V + 1)]
edges = []
answers = []

for _ in range(E):
    A, B, C = map(int, input().rstrip().split())
    heapq.heappush(edges, (C, A, B))

def find(idx):
    parent = idx
    while parent != groups[parent]:
        parent = groups[parent]

    groups[idx] = parent

    return parent

def union(A, B):
    parent_A = find(A)
    parent_B = find(B)

    if parent_A < parent_B:
        groups[parent_B] = parent_A
    else:
        groups[parent_A] = parent_B

while edges:
    weight, A, B = heapq.heappop(edges)
    # print(weight, A, B)

    if find(A) != find(B):
        answers.append(weight)
        union(A, B)
        # print(A, B)
        # print(groups[1:])

    if len(answers) == V - 1:
        break

print(sum(answers))
