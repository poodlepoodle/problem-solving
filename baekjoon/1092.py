from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
crains = list(map(int, input().rstrip().split()))
crains.sort(reverse=True)
MAX_WEIGHT = crains[0]
# print(crains)

M = int(input())
boxes = list(map(int, input().rstrip().split()))
boxes.sort(reverse=True)
boxes = deque(boxes)
# print(boxes)

buffer = deque()
time = 0
crain_idx = 0

while boxes:
    crain = crains[crain_idx]
    box = boxes[0]
    # print(f"{crain_idx}th crain({crain}) checks weight of box({box})...")

    if box > MAX_WEIGHT: break # 빠른 탈출 조건 
    if crain >= box:
        crain_idx += 1
        boxes.popleft()
    else:
        # print('  * X')
        buffer.append(boxes.popleft())
        # print(f'  * buffer: {buffer}')
    
    if crain_idx >= N or (not boxes and buffer):
        time += 1
        crain_idx = 0
        # print(f'all buffer items moves to box...')
        # print(f'  * buffer: {buffer}')
        while buffer:
            boxes.appendleft(buffer.pop())
        # print(f'  * boxes: {boxes}')
    
if crain_idx > 0: time += 1

if boxes: print(-1)
else: print(time)
