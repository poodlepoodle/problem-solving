# 백준 12869번: 뮤탈리스크

from collections import deque
from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())
SCVs = list(map(int, input().rstrip().split()))
SCVs.sort(reverse=True)
while len(SCVs) <= 3:
    SCVs.append(0)

# dp[i][j][k] = 1번째, 2번째, 3번째 SCV의 체력이 각각 i, j, k가 되기 위한 최소 공격 횟수
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
available_attacks = list(permutations([9, 3, 1], 3))

q = deque()
q.append((0, SCVs))
dp[SCVs[0]][SCVs[1]][SCVs[2]] = 1

answer = 0
while q and not answer:
    cnt, current_SCVs = q.popleft()
    # print(cnt, current_SCVs)

    for attacks in available_attacks:
        next_SCVs = sorted([max(0, current_SCVs[idx] - attacks[idx]) for idx in range(3)], reverse=True)
        if not dp[next_SCVs[0]][next_SCVs[1]][next_SCVs[2]]:
            if next_SCVs[0] == 0 and next_SCVs[1] == 0 and next_SCVs[2] == 0:
                answer = cnt + 1
                break
            else:
                dp[next_SCVs[0]][next_SCVs[1]][next_SCVs[2]] = cnt + 1
                q.append((cnt + 1, next_SCVs))

print(answer)
