import sys

def input(): return sys.stdin.readline().rstrip()

# 최대 10^4
N = int(input())

dices = []
for _ in range(N):
    A, B, C, D, E, F = map(int, input().split())
    # pair : A-F, B-D, C-E
    dices.append((A, B, C, F, D, E))

max_case_sum = 0

for i in range(6):
    bottom = dices[0][i]
    top = dices[0][(i + 3) % 6]

    case_sum = max([number for number in dices[0] if number != bottom and number != top])

    for j in range(1, N):
        bottom = top
        bottom_idx = dices[j].index(bottom)
        top = dices[j][(bottom_idx + 3) % 6]
        
        case_sum += max([number for number in dices[j] if number != bottom and number != top])

    max_case_sum = max(max_case_sum, case_sum)

print(max_case_sum)
