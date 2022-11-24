import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

numbers = input().split()

def compare(str1, str2):
    i, j = 0, 0

    while True:
        if str1[i] > str2[j]:
            return 1
        elif str1[i] < str2[j]:
            return -1

        if i == len(str1) - 1 and j == len(str2) - 1: break
        
        if i < len(str1) - 1:
            i += 1
        if j < len(str2) - 1:
            j += 1
    
    # 길이가 같을 경우는 더 긴 수 출력
    if len(str1) != len(str2):
        return 1 if len(str1) > len(str2) else -1
    return 0

for i in range(len(numbers), 1, -1):
    for j in range(i - 1):
        if compare(numbers[j], numbers[j + 1]) < 1:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

answer = ''
for number in numbers:
    answer += number
print(int(answer))
