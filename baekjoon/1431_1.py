# 백준 1431번: 시리얼 번호

import sys

input = sys.stdin.readline

N = int(input())
guitars = [input().rstrip() for _ in range(N)]
numbers = '1234567890'
guitars.sort(key=lambda x:(len(x), sum([int(s) for s in x if s in numbers]), x))
for guitar in guitars:
    print(guitar)
