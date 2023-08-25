# 백준 1700번: 멀티탭 스케줄링 (2회차)

from collections import deque
import sys

input = sys.stdin.readline

# N, K <= 10^2
N, K = map(int, input().rstrip().split())

orders = deque(list(map(int, input().rstrip().split())))

# 접근 1: 미래에 가장 멀리 사용하게 될 플러그를 빼기

plugged = []
answer = 0

while orders:
    number = orders.popleft()
    # print(number)

    # 1. 이미 해당 제품이 꽂혀 있는 경우
    if number in plugged:
        pass
    # 2. 콘센트 구멍이 남아 있는 경우
    elif len(plugged) < N:
        plugged.append(number)
    # 3. 뭔가를 빼고 꽂아야 할 경우
    else:
        replace_number, replace_idx = plugged[0], 0

        for plugged_number in plugged:
            # print(f"plugged: {plugged_number}")
            if plugged_number not in orders:
                replace_number, replace_idx = plugged_number, 0
                break
            else:
                appearance_idx = orders.index(plugged_number)

                if replace_idx < appearance_idx:
                    replace_number, replace_idx = plugged_number, appearance_idx
        
        plugged.remove(replace_number)
        plugged.append(number)
        answer += 1

    # print(plugged)
    # print()

print(answer)
