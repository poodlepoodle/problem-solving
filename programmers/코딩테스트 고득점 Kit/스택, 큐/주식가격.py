# 프로그래머스 42584번: 주식가격

def solution(prices):
    answer = []
    stack = [(len(prices) - 1, prices[-1] - 1)]
    
    for idx in range(len(prices) - 1, -1, -1):
        # print(idx)
        current_price = prices[idx]
        
        while stack and stack[-1][1] >= current_price:
            stack.pop()
            
        if len(stack) == 0: answer.append(len(prices) - 1 - idx)
        else: answer.append(stack[-1][0] - idx)
        stack.append((idx, current_price))
        # print(answer)
        # print(stack)
        # print()
    
    return answer[::-1]
