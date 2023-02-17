import sys
from itertools import combinations

def input(): return sys.stdin.readline().rstrip()

L, C = map(int, input().split())

candidates = list(input().split())

mos = ['a', 'e', 'i', 'o', 'u']

answers = []
for candidate in combinations(candidates, L):
    cand = list(candidate)
    ja_cnt = 0
    mo_cnt = 0
    
    for letter in cand:
        if letter in mos:
            mo_cnt += 1
        else:
            ja_cnt += 1
        
    if mo_cnt >= 1 and ja_cnt >= 2:
        cand.sort()
        answers.append("".join(cand))

answers.sort()
for ans in answers:
    print(ans)
