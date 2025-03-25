# 백준 1963번: 소수 경로

from collections import deque
import sys

input = sys.stdin.readline

def isPrime(number):
    number = int(number)
    for i in range(2, number // 2 + 1):
        if number % i == 0: return False
    return True

primes = {str(number): isPrime(number) for number in range(1000, 9999 + 1)}

T = int(input())
for _ in range(T):
    A, B = input().rstrip().split()

    q = deque()
    visited = {str(number): False for number in range(1000, 9999 + 1)}

    q.append((0, A))
    visited[A] = True

    answer = 10001
    while q:
        cnt, current = q.popleft()
        # print(cnt, current)

        if current == B:
            answer = cnt
            break

        for first in range(1, 10):
            next = str(first) + current[1:]
            if primes[next] and not visited[next]:
                q.append((cnt + 1, next))
                visited[next] = True

        for second in range(0, 10):
            next = current[:1] + str(second) + current[2:]
            if primes[next] and not visited[next]:
                q.append((cnt + 1, next))
                visited[next] = True

        for third in range(0, 10):
            next = current[:2] + str(third) + current[3:]
            if primes[next] and not visited[next]:
                q.append((cnt + 1, next))
                visited[next] = True

        for fourth in range(0, 10):
            next = current[:3] + str(fourth)
            if primes[next] and not visited[next]:
                q.append((cnt + 1, next))
                visited[next] = True

        if answer != 10001: break

    print(answer if answer != 10001 else 'Impossible')
