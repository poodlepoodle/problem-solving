# 백준 1935번: 후위 표기식2

from collections import deque
import sys

input = sys.stdin.readline

alphabets = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
variables = { key: None for key in alphabets}
operators = '+-*/'

N = int(input()) # <= 28
formulas = deque((input().rstrip()))
for idx in range(N):
    variables[alphabets[idx]] = int(input())
# print(variables)

def calc(operator, A, B):
    if operator == '+': return A + B
    elif operator == '-': return A - B
    elif operator == '*': return A * B
    elif operator == '/': return A / B
    return 0

stack = []
for item in formulas:
    if item in operators:
        B = stack.pop()
        A = stack.pop()
        stack.append(calc(item, A, B))
    else:
        stack.append(int(variables[item]))
    # print(item, stack)

print("%.2f" % stack[0])
