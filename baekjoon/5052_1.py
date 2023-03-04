from collections import deque
import sys
import pprint

input = sys.stdin.readline

for _ in range(int(input())): # 테스트 케이스 <= 50
    # N <= 10^4
    N = int(input())

    trie = {}
    consistency = True

    # 트라이에 모든 단어 입력하기
    for _ in range(N):
        number = input().rstrip()
        current = trie

        for letter in number:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        
        current['*'] = True
        
    q = deque([trie])

    while q:
        current = q.popleft()
        
        if '*' in current and len(current) >= 2:
            consistency = False
            break
        
        print(current)

        for key in current.keys():
            q.append(current[key])
    

    if consistency: print('YES')
    else: print('NO')

    # 여기까지 하는 데 12분 14초 소요
