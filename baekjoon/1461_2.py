# 백준 1461번: 도서관 (2회차)

import sys

input = sys.stdin.readline

# N, M <= 50
N, M = map(int, input().rstrip().split())

books = list(map(int, input().rstrip().split()))

right_books = [book for book in books if book > 0]
left_books = [-book for book in books if book < 0]

right_books.sort()
left_books.sort()

# print(right_books)
# print(left_books)

costs = []

# 오른쪽(양수 거리) 책 정리
idx = len(right_books) - 1

while idx >= M - 1:
    costs.append(right_books[idx])
    idx -= M

if idx >= 0:
    costs.append(right_books[idx])

# 왼쪽(음수 거리) 책 정리
idx = len(left_books) - 1

while idx >= M - 1:
    costs.append(left_books[idx])
    idx -= M

if idx >= 0:
    costs.append(left_books[idx])

# print(costs)

print(sum(costs) * 2 - max(costs))
