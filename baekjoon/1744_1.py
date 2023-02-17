import sys

input = sys.stdin.readline

# 최대 50
N = int(input())

numbers = [int(input()) for _ in range(N)]

# 그리디 전략
# 1. 양수는 큰 순서대로 묶어서 곱하기
# 2. 음수는 작은 순서대로 묶어서 곱하기
# 3. 0은 음수 쪽에 포함되도록 함
positives = [i for i in numbers if i > 0]
negatives = [i for i in numbers if i <= 0]

positives.sort(reverse=True)
negatives.sort()

answer = 0

# 양수 처리
idx = 0
while idx + 1 < len(positives):
    if positives[idx] == 1 or positives[idx + 1] == 1:
        answer += (positives[idx] + positives[idx + 1])
    else:
        answer += (positives[idx] * positives[idx + 1])
    idx += 2

# 남은 거는 그냥 더해주기
if idx < len(positives):
    answer += positives[idx]

# 음수 처리
idx = 0
while idx + 1 < len(negatives):
    answer += (negatives[idx] * negatives[idx + 1])
    idx += 2

# 남은 거는 그냥 더해주기
if idx < len(negatives):
    answer += negatives[idx]

# 정답 출력
print(answer)
