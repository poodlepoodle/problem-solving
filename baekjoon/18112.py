# 백준 18112번: 이진수 게임

# 딱 봐도 BFS이나.. 포인트는
# "이진수를 문자열로 계산하는 부분이 필요하다면, 시간복잡도 내에 통과할까?"

from collections import deque
import sys

input = sys.stdin.readline

start = int('0b' + input().rstrip(), base=2)
target = int('0b' + input().rstrip(), base=2)

q = deque()
q.append((start, 0))
visited = {}
visited[start] = True

def invert_single_bit(current):
    nexts = []
    # 한 자리 숫자를 보수로 바꾸기. 단, 맨 앞 숫자(Most Significant Digit)는 바꿀 수 없다.
    for i in range(len(bin(current)[2:]) - 1):
        nexts.append(current ^ (1 << i))
    return nexts

answer = -1
while q:
    current, cnt = q.popleft()
    # print(current, cnt)

    if current == target:
        answer = cnt
        break

    candidates = set()

    for item in invert_single_bit(current):
        candidates.add(item)
    candidates.add(current + 1)
    if current > 0: candidates.add(current - 1)
    
    # print('   * candidates:')
    for cand in candidates:
        if cand not in visited:
            # print('    ', cand)
            q.append((cand, cnt + 1))
            visited[cand] = True
    # print(q)

print(answer)
