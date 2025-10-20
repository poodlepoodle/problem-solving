# 백준 2205번: 저울 추 만들기

from collections import defaultdict
import sys

input = sys.stdin.readline

# N <= 10^4
N = int(input())

# 납덩어리의 종류: 1g, 2g, 3g, ..., ng
# 주석덩어리의 종류: 1g, 2g, 3g, ..., ng
# 가능한 조합 (x, y), (y, x)
# 목표: 2의 거듭제곱 (2, 4, 8, ...)

# 포인트: 다른 조합에 사용한 특정 무게는 재사용할 수 없음
# 가능한 여러 조합을 만들 수 있도록 잘 분배해야 함 -> DP?
# 근데 DP로 하려면 "조합 가능한 경우의 수"라면 더 어울릴 텐데...

# N = 8으로 가정
# X = 1: 1, 3, 7
# X = 2: 2, 6
# X = 3: 1, 5
# X = 4: 4
# X = 5: 3
# X = 6: 2
# X = 7: 1
# X = 8: 8
# N = 11으로 가정
# X = 1: 1, 3, 7
# X = 2: 2, 6
# X = 3: 1, 5
# X = 4: 4
# X = 5: 3, 11
# X = 6: 2, 10
# X = 7: 1, 9
# X = 8: 8
# X = 9: 7
# X = 10: 6
# X = 11: 5
# 관측: X가 커질수록 가능한 Y의 후보군은 줄어들고 있음

candidates = defaultdict(list)

threshold = 2
while True:
    for i in range(1, N + 1):
        if 0 < threshold - i <= N:
            candidates[i].append(threshold - i)
    if threshold > N: break
    threshold *= 2

# for key, value in candidates.items():
#     print(key, value)

used = {i: False for i in range(1, N + 1)}
answer = []
for x in range(N, 0, -1):
    for y in candidates[x][::-1]:
        if not used[y]:
            answer.append(y)
            used[y] = True
            break

for y in answer[::-1]:
    print(y)
