# 백준 1068번: 트리

from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
childs = defaultdict(list)
parents = list(map(int, input().rstrip().split()))
deletedNode = int(input())
root = -1

for child, parent in enumerate(parents):
    if parent == -1: root = child
    elif child != deletedNode: childs[parent].append(child)

answer = 0
def dfs(current):
    # print(f'dfs({current})')
    if len(childs[current]) == 0:
        global answer
        answer += 1
        return

    for child in childs[current]:
        dfs(child)

if deletedNode == root: print(0)
else:
    dfs(root)
    print(answer)
