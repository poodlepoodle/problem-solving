# 프로그래머스 43162번: 네트워크 풀이

from collections import defaultdict, deque

def solution(n, computers):
    answer = 0    
    networks = defaultdict(list)
    visited = [False for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            if i == j: continue
            if computers[i][j]:
                networks[i].append(j)
                networks[j].append(i)
                
    def bfs(start):
        nonlocal networks, visited
        q = deque()
        q.append(start)
        visited[start] = True
        
        while q:
            current = q.popleft()
            
            for node in networks[current]:
                if not visited[node]:
                    q.append(node)
                    visited[node] = True
                
    for current in range(n):
        if not visited[current]:
            bfs(current)
            answer += 1
        
    return answer
