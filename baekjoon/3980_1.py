import sys

def input(): return sys.stdin.readline().rstrip()

# 각 선수 별로 최대 가능한 포지션은 5개

def bruteforcing(visited, number):
    # print(f"bruteforcing({number}, {sum})")

    if number >= 11:
        global answer
        answer = max(answer, sum(visited))
        return

    for i in range(11):
        if scores[number][i] != 0 and not visited[i]:
            new_visited = visited.copy()
            new_visited[i] = scores[number][i]
            bruteforcing(new_visited, number + 1)

for _ in range(int(input())):
    scores = [list(map(int, input().split())) for _ in range(11)]
    
    answer = 0
    bruteforcing([False for _ in range(11)], 0)
    print(answer)
