# 백준 14500번: 테트로미노 (3회차)

import sys

input = sys.stdin.readline

# N, M <= 5 * 10^2
N, M = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

# R_SIZE, C_SIZE,
# each coordinates of SHAPES...
tetrominos = (
    # ####
    (
        1, 4,
        (
            (0, 0),
            (0, 1),
            (0, 2),
            (0, 3),
        )
    ),
    # #
    # #
    # #
    # #
    (
        4, 1,
        (
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
        )
    ),
    # ##
    # ##
    (
        2, 2,
        (
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
        )
    ),
    # #
    # #
    # ##
    (
        3, 2,
        (
            (0, 0),
            (1, 0),
            (2, 0),
            (2, 1),
        )
    ),
    #  #
    #  #
    # ##
    (
        3, 2,
        (
            (2, 0),
            (0, 1),
            (1, 1),
            (2, 1),
        )
    ),
    # ##
    #  #
    #  #
    (
        3, 2,
        (
            (0, 0),
            (0, 1),
            (1, 1),
            (2, 1),
        )
    ),
    # ##
    # #
    # #
    (
        3, 2,
        (
            (0, 0),
            (0, 1),
            (1, 0),
            (2, 0),
        )
    ),
    # ###
    # #
    (
        2, 3,
        (
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
        )
    ),
    # ###
    #   #
    (
        2, 3,
        (
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 2),
        )
    ),
    #   #
    # ###
    (
        2, 3,
        (
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
        )
    ),
    # #
    # ###
    (
        2, 3,
        (
            (0, 0),
            (1, 0),
            (1, 1),
            (1, 2),
        )
    ),
    #  #
    #  ##
    #   #
    (
        3, 2,
        (
            (0, 0),
            (1, 0),
            (1, 1),
            (2, 1),
        )
    ),
    #   #
    #  ##
    #  #
    (
        3, 2,
        (
            (0, 1),
            (1, 0),
            (1, 1),
            (2, 0),
        )
    ),
    #   ##
    #  ##
    (
        2, 3,
        (
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
        )
    ),
    #  ##
    #   ##
    (
        2, 3,
        (
            (0, 0),
            (0, 1),
            (1, 1),
            (1, 2),
        )
    ),
    #   #
    #  ###
    (
        2, 3,
        (
            (0, 1),
            (1, 0),
            (1, 1),
            (1, 2),
        )
    ),
    #  ###
    #   #
    (
        2, 3,
        (
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 1),
        )
    ),
    #  #
    #  ##
    #  #
    (
        3, 2,
        (
            (0, 0),
            (1, 0),
            (2, 0),
            (1, 1),
        )
    ),
    #   #
    #  ##
    #   #
    (
        3, 2,
        (
            (1, 0),
            (0, 1),
            (1, 1),
            (2, 1),
        )
    ),
)

answer = 0
for tetromino in tetrominos:
    SIZE_R, SIZE_C, shapes = tetromino
    # print(SIZE_R, SIZE_C)
    # print(shapes)

    for start_r in range(N - SIZE_R + 1):
        for start_c in range(M - SIZE_C + 1):
            # print(start_r, start_c)
            current_answer = 0
            
            for r, c in shapes:
                current_answer += board[start_r + r][start_c + c]
            
            # if answer < current_answer:
                # print(f'* new answer: {current_answer} <-', start_r, start_c, shapes, current_answer)
            answer = max(answer, current_answer)

    # print()

print(answer)
