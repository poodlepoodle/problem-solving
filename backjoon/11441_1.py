import sys

input = sys.stdin.readline

# 수의 개수 N: 최대 10^5
N = int(input())
numbers = list(map(int, input().rstrip().split()))

# 구간의 개수 M: 최대 10^5
M = int(input())

# 접근:
# 단순히 모든 M개의 구간마다 최대 N개 요소의 부분합을 훑는다면
# 10^5 * 10^5로 10^8 초과 -> 시간 초과
# M개의 구간을 줄이거나, 구간마다 N개의 요소를 훑는 경우 둘 중 하나를 O(logN) 이하로 줄여야 함

prefix_sums = [0]
for number in numbers:
    prefix_sums.append(prefix_sums[-1] + number)
# print(prefix_sums)

for _ in range(M):
    # 구간의 시작 i, 끝 j
    i, j = map(int, input().rstrip().split())

    # i부터 시작해 j까지의 구간 합:
    # prefix_sums[j] - prefix_sums[i - 1]
    print(prefix_sums[j] - prefix_sums[i - 1])
