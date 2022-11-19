import sys

def input(): return sys.stdin.readline().rstrip()

# 도시의 갯수 : 최대 10^2
N = int(input())

# 버스의 갯수 : 최대 10^5
M = int(input())

INF = int(1e9)
distance = [[INF for _ in range(N)] for _ in range(N)]

# 자기 자신으로 향하는 경로 0으로 초기화
for i in range(N):
    distance[i][i] = 0

# 간선 정보 입력
for _ in range(M):
    A, B, cost = map(int, input().split())
    A, B = A - 1, B - 1

    if distance[A][B] > cost:
        distance[A][B] = cost

# 플로이드 워셜 알고리즘 수행
for k in range(N):
    for i in range(N):
        for j in range(N):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# 못 가는 길은 0으로 만들기
for i in range(N):
    for j in range(N):
        if distance[i][j] == INF:
            distance[i][j] = 0

# 결과 출력
for row in distance:
    print(*row)
