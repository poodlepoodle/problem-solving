# 프로그래머스 86052번: 빛의 경로 사이클

import sys
sys.setrecursionlimit(10**6)

def solution(grid):
    # 0: top, 1: right, 2: down, 3: left
    moves = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    )
    # direction_text = ['^', '>', 'v', '<']
    R = len(grid)
    C = len(grid[0])
    visited = [[0 for _ in range(C)] for _ in range(R)]
    
    def visit(r, c, direction):
        nonlocal visited
        visited[r][c] |= (1 << direction)
        
    def is_visit(r, c, direction):
        nonlocal visited
        return (visited[r][c] & (1 << direction)) != 0
    
    def shoot(start_r, start_c, r, c, direction, length):
        # print(f'* {direction_text[direction]} ({r}, {c})')
        
        current_mark = grid[r][c]
        if current_mark == 'S': next_direction = direction
        elif current_mark == 'L': next_direction = (direction + 3) % 4
        else: next_direction = (direction + 1) % 4
        
        dr, dc = moves[next_direction]
        next_r, next_c = (r + dr + R) % R, (c + dc + C) % C
        if not is_visit(next_r, next_c, next_direction):
            visit(next_r, next_c, next_direction)
            shoot(start_r, start_c, next_r, next_c, next_direction, length + 1)
        else:
            if next_r == start_r and next_c == start_c:
                nonlocal answer
                answer.append(length + 1)
                # print('* answer!:', length + 1)
            return
    
    answer = []
    for r in range(R):
        for c in range(C):
            for drc in range(4):
                if not is_visit(r, c, drc):
                    visit(r, c, drc)
                    shoot(r, c, r, c, drc, 0)
    
    answer.sort()
    return answer
