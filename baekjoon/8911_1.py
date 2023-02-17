import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

moves = ((0, 1), (1, 0), (0, -1), (-1, 0))

for _ in range(int(input())):
    commands = deque(input())

    turtle = [0, 0]
    turtle_top, turtle_bottom, turtle_left, turtle_right = 0, 0, 0, 0
    direction = 0 # 0부터 북 동 남 서

    while commands:
        command = commands.popleft()

        # F: 한 눈금 앞으로
        if command == 'F':
            turtle[0] += moves[direction][0]
            turtle[1] += moves[direction][1]
        # B: 한 눈금 뒤로
        elif command == 'B':
            turtle[0] += moves[(direction + 2) % 4][0]
            turtle[1] += moves[(direction + 2) % 4][1]
        # L: 왼쪽으로 90도 회전
        elif command == 'L':
            direction = (direction + 3) % 4
        # R: 오른쪽으로 90도 회전
        elif command == 'R':
            direction = (direction + 1) % 4

        turtle_top = max(turtle_top, turtle[1])
        turtle_bottom = min(turtle_bottom, turtle[1])
        turtle_right = max(turtle_right, turtle[0])
        turtle_left = min(turtle_left, turtle[0])

    print(abs(turtle_right - turtle_left) * abs(turtle_top - turtle_bottom))
