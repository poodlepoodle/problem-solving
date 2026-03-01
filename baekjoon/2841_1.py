# 백준 2841번: 외계인의 기타 연주

import sys

input = sys.stdin.readline

# N <= 5 * 10^5
# M <= 3 * 10^5
N, M = map(int, input().rstrip().split())

stacks = [[] for _ in range(N + 1)]
answer = 0

for _ in range(N):
    note, flat = map(int, input().rstrip().split())
    # print(note, flat)

    while stacks[note] and stacks[note][-1] > flat:
        stacks[note].pop()
        answer += 1
    
    if not stacks[note] or (stacks[note] and stacks[note][-1] < flat):
        stacks[note].append(flat)
        answer += 1

    # for stack in stacks:
    #     print(stack)
    # print(answer)
    # print()

print(answer)
