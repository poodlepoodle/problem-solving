# 백준 8983번: 사냥꾼 (2회차)

import sys

input = sys.stdin.readline

# M <= 10^5, N <= 10^5
M, N, L = map(int, input().rstrip().split())

shooters = list(map(int, input().rstrip().split()))
shooters.sort()

animals = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 문제 접근
# - 구해야 하는 것: N개의 동물 중 주어진 M개의 사대에서 사정거리 L로 잡을 수 있는 동물의 수
# - 두 가지 방식 가능
#   1. 각 사대마다, 잡을 수 있는 동물 순회하며 검사
#   2. 각 동물마다, 가장 가까운 사대를 순회하며 검사
#   - 2번 방식이 한 동물을 두 번 잡는 경우를 제외하기에 좀 더 편리해 보이긴 함
# - 각 사대나 동물에 대한 한 번의 순회: O(10^5)는 줄일 수 없음
#   - 2번의 경우를 이용하면, 각 동물마다 잡을 수 있는 가장 가까운 사대를 검사한다면 시간복잡도 줄일 수 있음
# - 쟁점은 모든 사대의 사정거리가 같다는 점
#   - 다시 말해 특정 동물의 입장에서 자신에게서 가장 가로 거리가 가까운 사대만을 고려해도 된다는 뜻

def isCatchable(ax, ay, L):
    if L < ay:
        return False

    xRange = L - ay
    sxLeft = ax - xRange
    sxRight = ax + xRange
    
    left, right = 0, M - 1

    while left <= right:
        middle = (left + right) // 2
        sxMiddle = shooters[middle]

        if sxLeft <= sxMiddle <= sxRight:
            return True
        elif sxMiddle < sxLeft:
            left = middle + 1
        else:
            right = middle - 1

answer = 0

for ax, ay in animals:
    catchable = isCatchable(ax, ay, L)
    if catchable:
        answer += 1

print(answer)
