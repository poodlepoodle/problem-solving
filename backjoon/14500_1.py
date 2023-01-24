import sys

input = sys.stdin.readline

# N, M <= 500
N, M = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

blocks = []
# ##
# ##
blocks.append(
    [[1, 1],
    [1, 1]],
)

# ####
blocks.append(
    [[1, 1, 1, 1]]
)
# #
# #
# #
# #
blocks.append(
    [[1], 
    [1], 
    [1], 
    [1]]
)

# #
# #
# ##
blocks.append(
    [[1, 0], 
    [1, 0], 
    [1, 1]]
)
# ###
# #
blocks.append(
    [[1, 1, 1], 
    [1, 0, 0]]
)
# ##
#  #
#  #
blocks.append(
    [[1, 1], 
    [0, 1], 
    [0, 1]]
)
#   #
# ###
blocks.append(
    [[0, 0, 1], 
    [1, 1, 1]]
)
#  #
#  #
# ##
blocks.append(
    [[0, 1], 
    [0, 1], 
    [1, 1]]
)
# #
# ###
blocks.append(
    [[1, 0, 0], 
    [1, 1, 1]]
)
# ##
# #
# #
blocks.append(
    [[1, 1], 
    [1, 0], 
    [1, 0]]
)
# ###
#   #
blocks.append(
    [[1, 1, 1], 
    [0, 0, 1]]
)

# ##
#  ##
blocks.append(
    [[1, 1, 0], 
    [0, 1, 1]]
)
#  #
# ##
# #
blocks.append(
    [[0, 1],
    [1, 1], 
    [1, 0]]
)
#  ##
# ##
blocks.append(
    [[0, 1, 1], 
    [1, 1, 0]]
)
# #
# ##
#  #
blocks.append(
    [[1, 0],
    [1, 1], 
    [0, 1]]
)

# #
# ##
# #
blocks.append(
    [[1, 0],
    [1, 1], 
    [1, 0]]
)
# ###
#  #
blocks.append(
    [[1, 1, 1],
    [0, 1, 0]]
)
#  #
# ##
#  #
blocks.append(
    [[0, 1],
    [1, 1], 
    [0, 1]]
)
#  #
# ###
blocks.append(
    [[0, 1, 0],
    [1, 1, 1]]
)

answer = 0

for block in blocks:
    block_r, block_c = len(block), len(block[0])
    # print(block_r, block_c)
    
    for r in range(N - block_r + 1):
        for c in range(M - block_c + 1):
            block_sum = 0

            for dr in range(block_r):
                for dc in range(block_c):
                    if block[dr][dc]:
                        block_sum += board[r + dr][c + dc]

            answer = max(answer, block_sum)

print(answer)
