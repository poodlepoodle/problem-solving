# 17140번: 이차원 배열과 연산

from collections import Counter
import sys

input = sys.stdin.readline

# R, C <= 10^2
tr, tc, tk = map(int, input().rstrip().split())
maps = [[0 for _ in range(100)] for _ in range(100)]

for r in range(3):
    maps[r][0], maps[r][1], maps[r][2] = map(int, input().rstrip().split())

R, C = 3, 3

def rSort():
    global R, C
    max_c = C

    for r in range(R): # 10^2
        # 기존 정보 카운팅
        counter = Counter(maps[r][:C])
        del counter[0]
        line = counter.most_common()
        line.sort(key=lambda x: (x[1], x[0]))

        # 새로운 값 할당
        c = 0
        while c < len(line): # 10^2
            maps[r][c * 2], maps[r][c  * 2 + 1] = line[c]
            c += 1

        c *= 2
        max_c = max(max_c, c)
        while c < max_c: # 10^2
            maps[r][c] = 0
            c += 1
    
    C = max(C, max_c)

answer = -1

# for row in maps[:R]:
#     print(row[:C])
# print()

for t in range(101): # 10^2
    if maps[tr - 1][tc - 1] == tk:
        answer = t
        break

    if R >= C:
        rSort()
    else:
        R, C, maps = C, R, list(map(list, zip(*maps)))
        rSort()
        R, C, maps = C, R, list(map(list, zip(*maps)))

    # for row in maps[:R]:
    #     print(row[:C])
    # print()

print(answer)
