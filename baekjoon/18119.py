# 백준 18119번: 단어 암기

# 각 쿼리마다 완전히 알고 있는 단어의 개수를 출력
# 브루트포싱 -> M개의 쿼리마다 N개의 단어의 길이 10^3 모두 순회 -> 불가능
# 비트마스킹 필요할 듯

import sys

input = sys.stdin.readline

# N, M <= 10^4
N, M = map(int, input().rstrip().split())

alphabets = 'abcdefghijklmnopqrstuvwxyz'
bit_order = {key: order for order, key in enumerate(alphabets)}

dictionary = []
for _ in range(N):
    word = 0
    for letter in input().rstrip():
        word |= (1 << bit_order[letter])

    dictionary.append(word)

# 초기에는 모든 알파벳을 알고 있는 상태
known = (1 << 26) - 1
# print(bin(known)[2:])

for _ in range(M):
    _, letter = input().rstrip().split()
    known ^= (1 << bit_order[letter])
    # print(bin(known)[2:])

    answer = 0
    for word in dictionary:
        if (known & word) == word: answer += 1
    print(answer)
