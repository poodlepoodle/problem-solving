import sys

def input(): return sys.stdin.readline().rstrip()

# N, K는 최대 3 * 10^5
N, K = map(int, input().split())

kids = list(map(int, input().split()))

diffs = []
for i in range(1, N):
    diffs.append(kids[i] - kids[i - 1])

diffs.sort()
print(sum(diffs[:N - K]))
