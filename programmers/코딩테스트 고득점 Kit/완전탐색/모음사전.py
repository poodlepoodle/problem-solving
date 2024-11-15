# 프로그래머스 84512번: 모음사전 풀이

from collections import defaultdict
import sys

sys.setrecursionlimit(10**5)

letters = ['A', 'E', 'I', 'O', 'U']
table = defaultdict(int)
order = 1

def traversal(current):
    global order
    table[current] = order
    # print(current, order)
    order += 1
    
    if len(current) > 4: return
    
    for letter in letters:
        traversal(current + letter)

def solution(word):
    for letter in letters:
        traversal(letter)

    return table[word]
