# 백준 2866번: 문자열 잘라내기

import sys

input = sys.stdin.readline

# R, C <= 10^3
R, C = map(int, input().rstrip().split())
table = [list(input().rstrip()) for _ in range(R)]

def check_duplication(start_R): # 10^6
    dictionary = set()
    # print(start_R)

    for c in range(C):
        string = ''
        for r in range(start_R, R):
            string += table[r][c]
        # print(string)
        if string in dictionary:
            # print(False)
            return False
        dictionary.add(string)
    # print(True)
    # print()
    return True

answer = 0
start, end = 0, R - 1
while start <= end:
    middle = (start + end) // 2
    # print(middle)

    if not check_duplication(middle):
        end = middle - 1
    else:
        answer = max(answer, middle)
        start = middle + 1

print(answer)
