# 백준 3078번: 좋은 친구

from collections import defaultdict
import sys

input = sys.stdin.readline

# N, K <= 3 * 10^5
N, K = map(int, input().rstrip().split())
names = [len(input().rstrip()) for _ in range(N)]
# print(names)

# '좋은 친구'의 2가지 조건
#   1. 인덱스(등수) 차이가 K 이하일 것
#   2. 글자수가 같을 것

# 브루트포싱의 시간복잡도
#   각 사람마다 나머지 사람에 대해서 조사 -> O(N^2)
# 정렬되어 있다는 특성이 있으므로 슬라이딩 윈도우로 접근해야 할 듯.. 어떤 방법이든 O(N^2)보다는 작아야 함

left, right = 0, 1
freq = defaultdict(int)
freq[names[0]] = 1
answer = 0

while left < right and right < N:
    # print(left, right)
    if right - left <= K:
        answer += freq[names[right]]
        freq[names[right]] += 1
        # print(f'answer: {answer}')
        right += 1
    else:
        freq[names[left]] -= 1
        left += 1

print(answer)
