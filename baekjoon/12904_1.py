# 백준 12904번: A와 B

import sys

input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

answer = False

while T:
    if S == T:
        answer = True
        break
    
    if T[-1] == 'A':
        T = T[:-1]
    else: # T[-1] == 'B'
        T = T[:-1]
        T = T[::-1]

print(1 if answer else 0)
