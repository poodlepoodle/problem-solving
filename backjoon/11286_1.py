import sys
import heapq

def input(): return sys.stdin.readline().rstrip()

h = []

for _ in range(int(input())):
    number = int(input())

    if number == 0:
        if len(h) > 0:
            _, value = heapq.heappop(h)
            print(value)
        else:
            print(0)
        continue
    
    heapq.heappush(h, (abs(number), number))
