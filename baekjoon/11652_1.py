# 백준 11652번: 카드

import sys

input = sys.stdin.readline

# N <= 10^5
N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

answer, answer_freq = numbers[0], 1
current, current_freq = numbers[0], 1
ptr = 1
while ptr < N:
    if numbers[ptr] != current:
        if current_freq > answer_freq:
            answer, answer_freq = current, current_freq    
        current, current_freq = numbers[ptr], 1
    else:
        current_freq += 1
    ptr += 1

if current_freq > answer_freq:
    answer, answer_freq = current, current_freq    

print(answer)
