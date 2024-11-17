# 프로그래머스 42587번: 프로세스 풀이

def solution(priorities, location):
    from collections import deque
    import heapq
    answer = 1
    processQ = deque()
    priorityQ = []
    
    for idx, pri in enumerate(priorities):
        processQ.append((idx, pri))
        heapq.heappush(priorityQ, (-pri, idx))
        
    while processQ:
        idx, pri = processQ.popleft()
        # print(idx)
        
        if pri < -priorityQ[0][0]:
            processQ.append((idx, pri))
            continue
        
        heapq.heappop(priorityQ)
        if idx == location:
            break
        answer += 1
        
    return answer
