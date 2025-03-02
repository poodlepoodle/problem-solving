# 백준 14719번: 빗물

import sys

input = sys.stdin.readline

H, W = map(int, input().rstrip().split())
blocks = list(map(int, input().rstrip().split()))

stack = [(0, blocks[0])]
answer = 0

for idx in range(1, len(blocks)):
    right_block = blocks[idx]
    # print('current:', idx)

    while stack and stack[-1][1] <= right_block:
        middle_idx, middle_block = stack.pop()
        if stack:
            left_idx, left_block = stack[-1]
            # print(left_block, middle_block, right_block)

            width = idx - left_idx - 1
            height = left_block - middle_block if left_block <= right_block else right_block - middle_block
            answer += width * height

    stack.append((idx, right_block))
    # print(stack)
    # print(answer)
    # print()

print(answer)
