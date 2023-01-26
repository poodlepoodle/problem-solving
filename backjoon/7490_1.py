import sys

input = sys.stdin.readline

def bruteforcing(strings, idx, sums, last_operator, last_operand):
    if idx == N:
        if sums == 0:
            answers.append(strings)
        return
    
    # 더하기
    bruteforcing(strings + '+' + str(numbers[idx]), idx + 1, sums + numbers[idx], '+', str(numbers[idx]))

    # 빼기
    bruteforcing(strings + '-' + str(numbers[idx]), idx + 1, sums - numbers[idx], '-', str(numbers[idx]))
    
    # 공백
    if last_operator == '+':
        bruteforcing(strings + ' ' + str(numbers[idx]), idx + 1, sums - int(last_operand) + int(last_operand + str(numbers[idx])), last_operator, last_operand + str(numbers[idx]))
    elif last_operator == '-':
        bruteforcing(strings + ' ' + str(numbers[idx]), idx + 1, sums + int(last_operand) - int(last_operand + str(numbers[idx])), last_operator, last_operand + str(numbers[idx]))

# 최대 10
for _ in range(int(input())):
    # 최대 9
    N = int(input())

    numbers = list(range(1, N + 1))

    # 수열은 최대 9개 -> 연산자는 8개 배치 가능
    # 각 연산자는 3종류(더하기, 빼기, 공백) 가능 -> 3^8 = 6561 < 10^4
    # 테스트 케이스 10개 -> 10^5 : 브루트포싱 가능
    
    answers = []
    bruteforcing(str(numbers[0]), 1, numbers[0], '+', str(numbers[0]))
    answers.sort()
    
    for ans in answers:
        print(ans)
    print()
