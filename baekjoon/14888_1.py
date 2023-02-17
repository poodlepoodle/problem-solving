import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# N은 최대 11
N = int(input())

operands = list(map(int, input().rstrip().split()))
operators = list(map(int, input().rstrip().split()))

# 식을 만들 수 있는 모든 경우의 수 : N! -> 39916800 <= 10^8
# -> 브루트포싱 + 약간의 백트래킹만 잘 조지면 가능할듯...

def bruteforcing(idx, remains, result):
    if idx >= N:
        global mins, maxs
        maxs = max(maxs, result)
        mins = min(mins, result)
        return

    if remains[0] > 0:
        new_remains = remains.copy()
        new_remains[0] -= 1
        bruteforcing(idx + 1, new_remains, result + operands[idx])
    if remains[1] > 0:
        new_remains = remains.copy()
        new_remains[1] -= 1
        bruteforcing(idx + 1, new_remains, result - operands[idx])
    if remains[2] > 0:
        new_remains = remains.copy()
        new_remains[2] -= 1
        bruteforcing(idx + 1, new_remains, int(result * operands[idx]))
    if remains[3] > 0:
        new_remains = remains.copy()
        new_remains[3] -= 1
        bruteforcing(idx + 1, new_remains, int(result / operands[idx]))

mins = 1e9
maxs = -1e9

bruteforcing(1, operators.copy(), operands[0])

print(maxs)
print(mins)
