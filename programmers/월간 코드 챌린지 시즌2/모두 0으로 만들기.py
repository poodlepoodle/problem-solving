# 프로그래머스 76503번: 모두 0으로 만들기 풀이

# 정점의 개수 3 * 10^5, 간선의 개수 3 * 10^5 - 1
# 모든 정점을 타고 다니면서 시뮬레이션하는 건 거의 불가능? -> 법칙이 있지 않을까..
# '연산'을 이해해 본다면 아래와 같은 조건이 필요
#   1. 모든 정점의 가중치 합은 0이어야 함
#   2. 가중치는 리프 노드부터 부모 노드로 몰아주는 형태로 이어지는 것이 효율적임
#   3. 결국 모든 가중치 합이 0이면서, 마지막에 1개 노드로 가중치가 모아질 수 있는 최소 이동 횟수를 구하는 것

# MST? 다익스트라? Union-find?
# -> DFS!!

def solution(a, edges):
    if sum(a) != 0: return -1
    
    from collections import defaultdict
    import sys
    
    sys.setrecursionlimit(10**6)
    
    N = len(a)
    childs = defaultdict(list)
    visited = [False for _ in range(N)]
    answer = 0
    
    for A, B in edges:
        childs[A].append(B)
        childs[B].append(A)
        
    def dfs(current):
        nonlocal answer
        visited[current] = True
        
        for child in childs[current]:
            if not visited[child]:
                a[current] += dfs(child)

        answer += abs(a[current])
        return a[current]
    
    dfs(0)
    return answer
