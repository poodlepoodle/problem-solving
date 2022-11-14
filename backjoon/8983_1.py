import sys

def input(): return sys.stdin.readline().rstrip()

M, N, L = map(int, input().split())

places = list(map(int, input().split()))
places.sort()

animals = [tuple(map(int, input().split())) for _ in range(N)]

# 사대의 갯수 : 10^5
# 동물의 갯수 : 10^5

# 전략 1 : 모든 사대마다 사정거리 안에 있는 동물 체크 -> 10^10 -> 불가능
# 전략 2 : 모든 동물마다 사대의 사정거리 안에 있는지 체크 -> 10^5 * (L - 동물의 y좌표) -> 일단 L 들어가는 데서 무조건 불가능

# 직감 : 사대의 갯수나 동물의 갯수 중 하나만 logN으로 내리면 괜찮을 거 같은데... -> 이분 탐색?

count = 0

for x, y in animals:
    dx = L - y

    left = x - dx
    right = x + dx

    start = 0
    end = M - 1
    shoot = False

    while start <= end:
        middle = (start + end) // 2

        if left <= places[middle] <= right:
            shoot = True
            break
        elif places[middle] < left:
            start = middle + 1
        else: # right < places[middle]
            end = middle - 1

    if shoot:
        count += 1

print(count)
