import sys
import heapq

def input(): return sys.stdin.readline().rstrip()

N, centi, T = map(int, input().split())

giants = []
for _ in range(N):
    heapq.heappush(giants, -int(input()))

cnt = 0
while cnt < T:
    # 현재 기준 가장 큰 놈을 꺼내서
    giant = -heapq.heappop(giants)

    # 1. 만약 이미 센티보다 작아진 경우거나 2. 만약 1센티라 더 못때리면
    if giant < centi or giant == 1:
        heapq.heappush(giants, -giant)
        break

    # 이런 경우를 제외하고는 때린 다음 다시 힙에 넣어준다
    heapq.heappush(giants, -(giant // 2))
    cnt += 1

giant = -heapq.heappop(giants)
if giant < centi:
    print('YES')
    print(cnt)
else:
    print('NO')
    print(giant)
