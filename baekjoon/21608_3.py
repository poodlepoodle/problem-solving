# 백준 21608번: 상어 초등학교 (3회차)

import sys

input = sys.stdin.readline

# N <= 20
N = int(input())
maps = [[False for _ in range(N)] for _ in range(N)]
students = []
favorites = {}
for _ in range(N**2):
    student_num, *student_favorites = map(int, input().rstrip().split())
    students.append(student_num)
    favorites[student_num] = student_favorites

# 브루트포싱
#   1. N**2명의 학생 자리를 정함 -> O(N^2)
#   2. 각 학생마다 모든 가능한 자리를 검사 -> O(N^2)
#   결론: O(N^4)

moves = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]

def print_seats():
    for row in maps:
        print(row)
    print()

def is_in_board(r, c):
    return 0 <= r < N and 0 <= c < N

def get_nearest_favorites(r, c, favorites):
    cnt = 0
    for dr, dc in moves:
        if is_in_board(r + dr, c + dc) and maps[r + dr][c + dc]:
            if maps[r + dr][c + dc] in favorites: cnt += 1
    return cnt

def get_nearest_empty_seats(r, c):
    cnt = 0
    for dr, dc in moves:
        if is_in_board(r + dr, c + dc):
            if not maps[r + dr][c + dc]: cnt += 1
    return cnt

def check_new_seat(favorites):
    max_favorites = -1
    max_emptys = -1
    seats = [-1, -1]

    for r in range(N):
        for c in range(N):
            if maps[r][c]: continue
            
            nearest_favorites = get_nearest_favorites(r, c, favorites)
            nearest_emptys = get_nearest_empty_seats(r, c)

            if nearest_favorites > max_favorites:
                # print(f'* 친한 친구가 {nearest_favorites}명으로 가장 많은 자리 -> {(r, c)}')
                max_favorites = nearest_favorites
                max_emptys = nearest_emptys
                seats = [r, c]
            elif nearest_favorites == max_favorites:
                if nearest_emptys > max_emptys:
                    # print(f'* 빈 자리가 {nearest_emptys}개로 가장 많은 자리 -> {(r, c)}')
                    max_emptys = nearest_emptys
                    seats = [r, c]

    return seats

def get_satisfying():
    sums = 0
    for r in range(N):
        for c in range(N):
            student_num = maps[r][c]
            student_favorites = favorites[student_num]
            score = get_nearest_favorites(r, c, student_favorites)

            if score >= 4: sums += 1000
            elif score >= 3: sums += 100
            elif score >= 2: sums += 10
            elif score: sums += 1
    return sums

for num in students:
    student_favorites = favorites[num]
    # print(f'{num}번 학생: {set(student_favorites)}')
    r, c = check_new_seat(set(student_favorites))
    maps[r][c] = num
    # print_seats()

print(get_satisfying())
