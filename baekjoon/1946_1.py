import sys

input = sys.stdin.readline

# 테스트 케이스 <= 2 * 10
for _ in range(int(input())):
    # N <= 10^5
    N = int(input())

    applicants = [list(map(int, input().rstrip().split())) for _ in range(N)]

    # 모든 면접자마다 다른 면접자들과 비교하는 건 10^5 * 10^5 = 10^10으로 초과
    # 정렬하면 10^5 * log (10^5)로 통과할 수 있을 것 같음

    applicants.sort(key=lambda x:x[0])

    passes = 1
    highest_second = applicants[0][1]

    for idx in range(1, len(applicants)):
        first, second = applicants[idx]

        # 내 순위가 다른 누군가보다 적어도 서류나 면접 둘 중 하나에서만이라도 떨어지지 않는 경우
        if second < highest_second:
            passes += 1
            highest_second = second

    print(passes)
