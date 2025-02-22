# 프로그래머스 42628번: 이중우선순위큐 풀이

import heapq

def solution(operations):
    minHeap = []
    maxHeap = []
    deletable = {}
    uniqueId = 0
    
    for op in operations:
        print(op)
        opcode, operand = op.split()
        operand = int(operand)
        
        if opcode == 'I': # 삽입
            heapq.heappush(minHeap, (operand, uniqueId))
            heapq.heappush(maxHeap, (-operand, uniqueId))
            deletable[uniqueId] = False
            uniqueId += 1
        elif opcode == 'D' and operand > 0: # 최댓값 삭제
            print('최댓값 삭제')
            while maxHeap:
                _, uid = heapq.heappop(maxHeap)
                if deletable[uid]:
                    del deletable[uid]
                    continue
                deletable[uid] = True
                break
            
        else: # 최솟값 삭제
            print('최솟값 삭제')
            while minHeap:
                _, uid = heapq.heappop(minHeap)
                if deletable[uid]:
                    del deletable[uid]
                    continue
                deletable[uid] = True
                break
        
        # print('minHeap:', minHeap)
        # print('maxHeap:', maxHeap)
        # print()

    while minHeap and deletable[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and deletable[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    
    if minHeap and maxHeap:
        minValue, _ = heapq.heappop(minHeap)
        maxValue, _ = heapq.heappop(maxHeap)
        return [-maxValue, minValue]
    return [0, 0]
