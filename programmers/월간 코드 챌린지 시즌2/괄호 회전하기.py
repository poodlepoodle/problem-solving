# 프로그래머스 76502번: 괄호 회전하기 풀이

from collections import deque

# 모든 회전 경우의 수 세는 데 -> 10^3
# 경우의 수마다 괄호 판단하는 데 -> 10^3

matches = {
    "]": "[",
    "}": "{",
    ")": "("
}

def isCorrectBraceString(string):
    stack = deque()
    
    for letter in string:
        if letter in [']', '}', ')']:
            if stack and stack.pop() == matches[letter]:
                pass
            else:
                return False
        else:
            stack.append(letter)
            
    if len(stack) != 0: return False
    return True

def solution(s):
    answer = 0
    string = s[:]
    
    for _ in range(len(s)):
        if isCorrectBraceString(string):
            answer += 1
        string = string[-1] + string[:-1]
    return answer
