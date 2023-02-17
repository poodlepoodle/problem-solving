import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

numbers = input().split()

def compare(str1, str2):
    max_len = max(len(str1), len(str2))
    idx = 0

    while True:
        if str1[idx % len(str1)] > str2[idx % len(str2)]: return 1
        elif str1[idx % len(str1)] < str2[idx % len(str2)]: return -1

        if idx >= 2 * len(str1) - 1 and idx >= 2 * len(str2) - 1: break
        
        idx += 1
    
    return 0

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if compare(numbers[j], numbers[j + 1]) < 1:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

answer = ''
for number in numbers:
    answer += number
print(int(answer))
