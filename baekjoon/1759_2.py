# 백준 1759번: 암호 만들기 (2회차)

from itertools import combinations
import sys

input = sys.stdin.readline

# L, C <= 15
L, C = map(int, input().rstrip().split())

# 최대 경우의 수: C개 중에서 L개를 선택하는 조합의 수 (순서가 정해져 있으므로)
# -> 15C7 or 15C8 <= 10^4
# 브루트포싱 적용

moeum_range = ('a', 'e', 'i', 'o', 'u')

characters = input().rstrip().split()
characters.sort()
jas = []
mos = []

for ch in characters:
    if ch in moeum_range:
        mos.append(ch)
    else:
        jas.append(ch)

for passwd in combinations(characters, L):
    ja_cnt = 0
    mo_cnt = 0

    for ch in passwd:
        if ch in moeum_range:
            mo_cnt += 1
        else:
            ja_cnt += 1
    
    if ja_cnt >= 2 and mo_cnt >= 1:
        print(*passwd, sep="")
