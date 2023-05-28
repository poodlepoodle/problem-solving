# 백준 5430번: AC

import sys

input = sys.stdin.readline

def AC(commands, len_arr):
    left, right = 0, len_arr
    front = True

    for comm in commands: # 10^5
        # print(comm)

        if comm == 'R':
            front = not front
        elif comm == 'D':
            if left >= right: return -1

            if front:
                left += 1
            else:
                right -= 1

        # print(front, left, right)

    return (front, left, right)

# T <= 10^2
for _ in range(int(input())):
    # P <= 10^5
    P = input().rstrip()
    
    # N <= 10^5
    N = int(input())

    arr = list(input().rstrip()[1:-1].split(","))
    if arr[0] == '':
        arr = []

    ac = AC(P, len(arr))

    if ac == -1:
        print("error")
        continue
    
    front, left, right = ac
    if not front:
        arr.reverse()
        left, right = N - right, N - left
    print(f'[{",".join(arr[left : right])}]')
