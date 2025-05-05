# 백준 2143번: 두 배열의 합 (2회차)

from collections import defaultdict
import sys

input = sys.stdin.readline

# 구간합 타겟 T <= 10^9
T = int(input())

# N, M <= 10^3
N = int(input())
A = list(map(int, input().rstrip().split()))
M = int(input())
B = list(map(int, input().rstrip().split()))

# 특정 배열의 모든 구간 합을 구하는 경우의 수 = O(N^2) = 10^6
# 두 배열의 구간 합을 구하는 경우의 수 = O(N^2 * N^2) = 10^12
# -> 줄여야 한다

# 특정 배열의 모든 구간 합을 prefix sum으로 구하고, 'T - sum(B[b1:b2])'를 구하도록 한다면?
# 주의사항: b1 == b2일 수 있음

prefixes_A = [0]
for a in A: # 10^3
    prefixes_A.append(prefixes_A[-1] + a)
prefixes_B = [0]
for b in B: # 10^3
    prefixes_B.append(prefixes_B[-1] + b)

set_A = set()
freq_A = defaultdict(int)
for i in range(1, N + 1): # 10^6
    for j in range(i):
        sum_A = prefixes_A[i] - prefixes_A[j]
        set_A.add(sum_A)
        freq_A[sum_A] += 1
set_B = set()
freq_B = defaultdict(int)
for i in range(1, M + 1): # 10^6
    for j in range(i):
        sum_B = prefixes_B[i] - prefixes_B[j]
        set_B.add(sum_B)
        freq_B[sum_B] += 1

if len(set_A) > len(set_B):
    set_A, freq_A, set_B, freq_B = set_B, freq_B, set_A, freq_A
list_A, list_B = list(set_A), list(set_B)
list_A.sort()
list_B.sort()

def bin_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target: return True
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False

answer = 0
for a in list_A:
    b = T - a
    
    if bin_search(list_B, b):
        answer += freq_A[a] * freq_B[b]

print(answer)
