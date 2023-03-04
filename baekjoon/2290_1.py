import sys

input = sys.stdin.readline

# S <= 10, N <= 10^10
S, N = input().rstrip().split()

S = int(S)
N = list(N)

rows = [[] for _ in range(2 * S + 3)]

for number in N:
    row_idx = 0

    if number == '1':
        rows[row_idx].append(' ' * (S + 2))
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' * (S + 2))
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' * (S + 2))
        row_idx += 1

    elif number == '2':
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + ' ')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

    elif number == '3':
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

    elif number == '4':
        rows[row_idx].append(' ' * (S + 2))
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + '|')
            row_idx += 1
        
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' * (S + 2))
        row_idx += 1

    elif number == '5':
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + ' ')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

    elif number == '6':
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + ' ')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

    elif number == '7':
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + ' ' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + ' ' * S + ' ')
        row_idx += 1

    elif number == '8':
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

    elif number == '9':
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append(' ' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

    elif number == '0':
        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + ' ' * S + ' ')
        row_idx += 1

        for _ in range(S):
            rows[row_idx].append('|' + ' ' * S + '|')
            row_idx += 1

        rows[row_idx].append(' ' + '-' * S + ' ')
        row_idx += 1

for row in rows:
    print(" ".join(row) + ' ')
