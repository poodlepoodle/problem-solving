from collections import deque
import sys

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

    # 트라이 순회하며 *가 있으면서 자식이 2개 이상 있는 노드 찾기 -> inconsistent point
    while q:
        current = q.popleft()
        
        # print(current)
        if len(current) >= 2 and '*' in current:
            consistency = False
            break

        for key, value in current.items():
            if key != '*':
                q.append(value)
    
    if consistency: print('YES')
    else: print('NO')
