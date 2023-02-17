# 2261번: 가장 가까운 두 점

# 서로 다른 점의 갯수 : 최대 10^5 (겹치는 점도 다른 점으로 봐야 함)
# 따라서 모든 두 점의 쌍 (A, B)에 대해 완전탐색은 불가능하다

import sys
sys.setrecursionlimit(10**5)

def input(): return sys.stdin.readline().rstrip()

# 점의 갯수 N : 최대 10^5
N = int(input())

# 점들의 정보 입력
points = [tuple(map(int, input().split())) for _ in range(N)]
# x축 기준 작은 순서로 정렬
points.sort(key = lambda x:(x[0], x[1]))

# 두 점 A, B의 유클리디안 거리 구하기
def distance(A, B):
    return (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2

def dnq(start, end):
    # print(f"dnq({start}, {end})")

    if end - start == 1:
        return distance(points[start], points[end])
    elif end - start == 2:
        return min(distance(points[end], points[end - 1]), distance(points[end - 1], points[start]), distance(points[end], points[start]))

    middle = start + (end - start) // 2
    middle_x = points[middle][0]
    # x축을 기준으로 분할 정복한 최솟값 구하기
    x_min = min(dnq(start, middle), dnq(middle + 1, end))

    # middle point를 중심으로 x축 좌우 방향으로 x_min 이내로 있는 점들만 집합
    additional_set = [(x, y) for x, y in points[start : end + 1] if (x - middle_x) ** 2 < x_min]

    # y축 기준 작은 순서로 정렬
    additional_set.sort(key = lambda x:x[1])

    y_min = x_min
    for i in range(len(additional_set) - 1):
        for j in range(i + 1, len(additional_set)):
            if (additional_set[i][1] - additional_set[j][1]) ** 2 >= y_min: break
            elif additional_set[i][0] <= middle_x and additional_set[j][0] <= middle_x: continue
            elif middle_x < additional_set[i][0] and middle_x < additional_set[j][0]: continue

            # print(y_min, " -> ", end = "")
            y_min = min(y_min, distance(additional_set[i], additional_set[j]))
            # print(y_min)

    return y_min
    
# point_set = tuple(set(points))
if len(points) != len(set(points)):
    print(0)
else:
    answer = dnq(0, N - 1)
    print(answer)
