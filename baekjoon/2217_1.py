# 백준 2217번: 로프

import sys

input = sys.stdin.readline

# N <= 10^5
N = int(input())
# rope_capacities[i] <= 10^4
rope_capacities = [int(input()) for _ in range(N)]

# 구해야 하는 것
#   - 이 로프들을 사용해 들 수 있는 최대 중량 
# 고려해야 하는 것
#   - 로프는 모두 사용하지 않아도 됨
#   - 로프 수가 좀 많음...
#   - 로프를 K개 병렬로 연결할 때, 들 수 있는 최대 중량은 (가장 낮은 로프 중량 * K)

rope_capacities.sort()
# print(rope_capacities)
answer = -1

for idx, rope in enumerate(rope_capacities):
    answer = max(answer, rope * (N - idx))

print(answer)
