# 프로그래머스 42583번: 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    trucks = deque(truck_weights)
    
    total_weight = 0
    t = 0
    
    while bridge or trucks:
        if bridge and t - bridge[0][1] >= bridge_length:
            passed_t_weight, _ = bridge.popleft()
            total_weight -= passed_t_weight
            
        if trucks:
            t_weight = trucks[0]
            
            if total_weight + t_weight <= weight:
                _ = trucks.popleft()
                bridge.append((t_weight, t))
                total_weight += t_weight
            
        # print(t)
        # print(list(bridge))
        # print(list(trucks))
        # print()
        
        t += 1
    
    return t
