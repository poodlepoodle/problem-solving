import sys
from itertools import combinations

def input(): return sys.stdin.readline().rstrip()

N = int(input())

numbers = list(map(int, input().split()))
created = set()

# 20C10 -> 20*19*18*...*10 / 9*8*7*...*2 -> 2 * 10^5
for i in range(1, N + 1):
    for subset in combinations(numbers, i):
        created.add(sum(subset))

i = 1
while i in created: i += 1
print(i)
