# 프로그래머스 43163번: 단어 변환

from collections import deque

def distance(w1, w2):
    cnt = 0
    for idx in range(len(w1)):
        if w1[idx] != w2[idx]:
            cnt += 1
    return cnt

def solution(begin, target, words):
    visited = {}
    for word in words:
        visited[word] = False
        
    q = deque()
    q.append((0, begin))
    visited[begin] = True
    # print(q)
    
    while q:
        cnt, current = q.popleft()
        
        for word in words:
            # print(current, word, distance(current, word))
            if distance(current, word) <= 1 and not visited[word]:
                if word == target: return cnt + 1
                q.append((cnt + 1, word))
                visited[word] = True
        # print(q)
    
    return 0
