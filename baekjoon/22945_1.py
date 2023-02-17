import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
X = list(map(int, input().split()))

# 팀의 능력치 : (개발자 A와 개발자 B 사이에 존재하는 다른 개발자 수) × min(개발자 A의 능력치, 개발자 B의 능력치)

# N은 최대 10^5 -> 모든 경우의 수 절대 탐색할 수 없음
# 적어도 더 나은 탐색만 세 나가도록 할 수는 있음

front, end = 0, N - 1
answer = -1

while front < end:
    
    score = (end - front - 1) * min(X[front], X[end])
    answer = max(answer, score)

    if X[front] < X[end]:
        front += 1
    else:
        end -= 1

print(answer)
