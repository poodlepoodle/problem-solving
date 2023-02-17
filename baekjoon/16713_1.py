import sys

input = sys.stdin.readline

# N은 최대 10^6, Q는 최대 3 * 10^6
N, Q = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

prefix_xors = [0]
for number in numbers:
    prefix_xors.append(prefix_xors[-1] ^ number)

answer = 0
for _ in range(Q):
    i, j = map(int, input().rstrip().split())

    answer ^= (prefix_xors[j] ^ prefix_xors[i - 1])

print(answer)
