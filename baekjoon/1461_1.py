import sys

input = sys.stdin.readline

# 책 개수 N, 최대 들 수 있는 개수 M <= 50
N, M = map(int, input().rstrip().split())

distances = list(map(int, input().rstrip().split()))

distances_right = [distance for distance in distances if distance > 0]
distances_left = [-distance for distance in distances if distance < 0]

distances_right.sort()
distances_left.sort()

# print(distances_right)
# print(distances_left)

answer = 0
comeback_distance = 0

idx = len(distances_right) - 1
while idx >= (M - 1):
    answer += distances_right[idx] * 2
    comeback_distance = max(comeback_distance, distances_right[idx])
    idx -= M

if idx >= 0:
    answer += distances_right[idx] * 2
    comeback_distance = max(comeback_distance, distances_right[idx])

idx = len(distances_left) - 1
while idx >= (M - 1):
    answer += distances_left[idx] * 2
    comeback_distance = max(comeback_distance, distances_left[idx])
    idx -= M

if idx >= 0:
    answer += distances_left[idx] * 2
    comeback_distance = max(comeback_distance, distances_left[idx])

print(answer - comeback_distance)
