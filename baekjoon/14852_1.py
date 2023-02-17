import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

# ㅁ
# ㅁ
dp_1_2 = [0] * (N + 1)
# ㅁㅁ
dp_2_1 = [0] * (N + 1)
# ㅁ
dp_1_1 = [0] * (N + 1)

# N = 1
# ㅁ
# ㅁ
dp_1_2[1] = 1
dp_1_1[1] = dp_1_2[1]

# N = 2
# ㅁㅁ
# ㅁㅁ
dp_1_2[2] = 1
dp_2_1[2] = 1
dp_1_1[2] = 2 * dp_1_2[2] + 2 * dp_2_1[2] + 1

# N = 3
# ㅁㅁㅁ
# ㅁㅁㅁ
dp_1_2[3] = 1
dp_2_1[3] = 4
dp_1_1[3] = 3 * dp_1_2[3] + 3 * dp_2_1[3] + 1