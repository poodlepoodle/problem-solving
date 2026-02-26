# 백준 1043번: 거짓말 (2회차)

import sys

input = sys.stdin.readline

# N, M <= 50
N, M = map(int, input().rstrip().split())
# 0 <= num_secret_members <= 50
num_secret_members, *secret_members = map(int, input().rstrip().split())

# 1차 접근
#   시간복잡도 계산
#   1. 모든 파티에 대해서 반복 -> 50
#   2. 모든 파티마다 각 사람에 대해서 반복 -> 50
#   3. 각 사람마다 비밀을 아는 자에 속하는지 검사 -> 50
#       3-1. 만약 해시처리한다면 O(1)
#   결론: 그냥 돌려도 통과는 될 듯 한데...
#       근데 문제는 특정 사람이 A 파티에서는 거짓말, B 파티에서는 진실을 듣는 경우도 제외해야 함
#   포인트
#   - 테스트 케이스 5를 참고하면.. 10 단독으로 먼저 만나지만 나중에 3 10 이렇게 한번 만나기 때문에
#         앞서 10 단독으로 얘기할 때도 거짓말은 할 수 없음

# 2차 접근
#   문제점
#       - [1, 2], [2, 3], [3, 4], [4, 5]로 파티가 구성되어 있고 5가 진실을 알고 있을 때
#         사실은 모두에게 말하면 안 되지만 1차 접근 코드로는 4만 진실을 알고 있다고 잘못 판단함
#   결론
#       - 유니온-파인드 써야 함...
#       - 대신 지금처럼 한 번 전체적으로 훑어서 판정하고 다시 파티를 순회하는 구조는 유지

parents = [idx for idx in range(N + 1)]

def find(x):
    if x == parents[x]: return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    A = find(a)
    B = find(b)

    if A < B: parents[B] = A
    elif A > B: parents[A] = B

parties = []
for _ in range(M):
    num_peoples, *peoples = map(int, input().rstrip().split())
    parties.append(peoples)

    if len(peoples) == 1: continue

    first, *peoples = peoples
    for person in peoples:
        union(first, person)

# print(parents)

cannot_tells = set()
for person in secret_members:
    cannot_tells.add(find(person))
# print(cannot_tells)

answer = 0
for peoples in parties:
    can_tell = True
    for person in peoples:
        if find(person) in cannot_tells:
            can_tell = False
            break
    
    # print(peoples, can_tell)
    answer += 1 if can_tell else 0

print(answer)
