from collections import defaultdict
import sys

input = sys.stdin.readline

# 최대 5 * 10^5
N, M = map(int, input().rstrip().split())

dicts = defaultdict(int)

# 듣도 못한 사람
for _ in range(N):
    name = input().rstrip()
    dicts[name] += 1

answers = []

# 보도 못한 사람
for _ in range(M):
    name = input().rstrip()
    if dicts[name] > 0:
        answers.append(name)

answers.sort()

# 정답 출력
print(len(answers))
for person in answers:
    print(person)
