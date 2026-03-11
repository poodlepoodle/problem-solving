# 백준 1946번: 신입 사원 (3회차)

import sys

input = sys.stdin.readline

# 접근
#   1. N명마다 나머지 N-1명과 모두 비교해버리면 O(N^2) = 10^10
#   2. 기준이 2개니까... 정렬을 한번 우선 해보고

# T <= 20
T = int(input())

for _ in range(T):
    # N <= 10^5
    N = int(input())
    ranks = [list(map(int, input().rstrip().split())) for _ in range(N)]
    ranks.sort(key=lambda x:(x[0]))
    # for rank in ranks:
    #     print(rank)

    # 그리디 전략: 뽑으면 안 되는 사람은 둘 모두 뒤처지는 '적어도 1명'이 있는 것
    #           즉, 1번째 성적 내림차순으로 정렬해서 2번째 성적만 지금까지의 최저보다 높은 사람만 골라가면 될듯?
    answer = 1
    highest_rank = ranks[0][1]
    for _, current_rank in ranks[1:]:
        if current_rank < highest_rank:
            answer += 1
        highest_rank = min(highest_rank, current_rank)

    print(answer)
