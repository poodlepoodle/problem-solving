# 백준 2179번: 비슷한 단어

from collections import defaultdict
import sys
input = sys.stdin.readline

# N <= 2 * 10^4
N = int(input())
# len(words[i]) <= 10^2
words = [input().rstrip() for _ in range(N)]
# for word in words:
#     print(word)

dicts = defaultdict(list)
for word in words:
    for idx in range(len(word)):
        prefix = word[:idx + 1]
        dicts[prefix].append(word)

answer_len = 0
answer = []
for key, value in dicts.items():
    if answer_len < len(key) and len(value) >= 2:
        answer_len = len(key)
        answer = [value[0], value[1]]

for word in answer:
    print(word)
