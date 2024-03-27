# 22945번: 팀 빌딩 (2회차)

import sys

input = sys.stdin.readline

N = int(input()) # <= 10^5
people = list(map(int, input().rstrip().split()))

# 포인트: 하나의 팀만 능력치를 몰빵한다면 그게 정답

if N == 2: print(0)
elif N == 3: print(min(people[0], people[2]))
else:
    answer = 0

    left = 0
    right = N - 1
    num_peoples = (right - left - 1)

    while num_peoples > 0:
        current_answer = num_peoples * min(people[left], people[right])
        answer = max(answer, current_answer)

        if people[left] < people[right]: left += 1
        elif people[left] > people[right]: right -= 1
        else:
            if people[left + 1] < people[right - 1]:
                right -= 1
            else:
                left += 1

        num_peoples -= 1

    print(answer)
