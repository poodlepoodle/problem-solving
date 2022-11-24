import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

numbers = input().split()

def compare(str1, str2):
    i, j = 0, 0

    while True:
        if str1[i % len(str1)] > str2[j % len(str2)]:
            return 1
        elif str1[i % len(str1)] < str2[j % len(str2)]:
            return -1

        if i >= 2 * len(str1) - 1 and j >= 2 * len(str2) - 1: break
        
        i += 1
        j += 1
    
    # return 0

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if compare(numbers[j], numbers[j + 1]) < 1:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

answer = ''
for number in numbers:
    answer += number
print(int(answer))
