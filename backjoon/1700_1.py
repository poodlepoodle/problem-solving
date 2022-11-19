import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

# 플러그 갯수 N, 전자제품 사용 횟수 K
N, K = map(int, input().split())

# ex : 2 3 2 3 1 2 7
order = list(map(int, input().split()))
# print(order)

using = []
cnt = 0

for i in range(len(order)):
    # print(using, end = ' ')

    current = order[i]
    # print(current)

    if current in using:
        continue
    elif len(using) < N:
        using.append(current)
    else:
        change_item = using[0]
        change_useage = -1
        for use in using:
            # print(use, ' will be reused in ', end = '')

            future_useage = 0
            for k in range(i + 1, len(order)):
                if order[k] == use:
                    break
                future_useage += 1
            # print(future_useage)

            if change_useage < future_useage:
                change_useage = future_useage
                change_item = use
        
        using.remove(change_item)
        using.append(current)
        cnt += 1

print(cnt)
