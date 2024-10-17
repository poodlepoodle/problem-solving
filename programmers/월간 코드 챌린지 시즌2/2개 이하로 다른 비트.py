# 프로그래머스 77885: 2개 이하로 다른 비트 풀이

# 10^15 크기의 수가 주어졌을 때, +1씩 더하는 건 시간이 너무 오래 소요됨
# '2개 이하'를 활용해 규칙을 찾아야 함
# 1. 가장 오른쪽의 0을 1로 바꾸기
# 2. 가장 오른쪽의 '1' 군집에서 가장 왼쪽을 0으로 바꾸기
# 일단은 이렇게 한 번 구현해 보고 추가 규칙을 찾아도 좋겠다고 생각함

def replaceLSBZero(binStr):
    string = binStr[:]
    idx = len(string) - 1
    
    while string[idx] != '0':
        idx -= 1
    string = string[:idx] + '1' + string[idx + 1:]
        
    return (idx, string)

def replaceMSBOne(startIdx, binStr):
    idx = startIdx + 1
    string = binStr[:]
    
    while idx < len(string) and string[idx] != '1':
        idx += 1
    if idx < len(string):
        string = string[:idx] + '0' + string[idx + 1:]
        
    return string

def solution(numbers):
    answer = []
    
    for number in numbers:
        binStr = bin(number)[2:].zfill(20)
        # print(binStr)
        idx, binStr = replaceLSBZero(binStr)
        # print(idx, binStr)
        binStr = replaceMSBOne(idx, binStr)
        # print(binStr)
        answer.append(int('0b' + binStr, 2))
        # print(answer)
        # print()
    
    return answer
