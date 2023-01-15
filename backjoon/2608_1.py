import sys

input = sys.stdin.readline

roma_1 = input().rstrip()
roma_2 = input().rstrip()

romas = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50,
        'C' : 100, 'D' : 500, 'M' : 1000,
        'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90,
        'CD' : 400, 'CM' : 900}

# 두 수를 아라비아 숫자로 변환
arabia_1 = 0
idx = 0
while idx < len(roma_1):
    if idx < len(roma_1) - 1 and roma_1[idx : idx + 2] in romas.keys():
        arabia_1 += romas[roma_1[idx : idx + 2]]
        idx += 2
    else:
        arabia_1 += romas[roma_1[idx]]
        idx += 1

arabia_2 = 0
idx = 0
while idx < len(roma_2):
    if idx < len(roma_2) - 1 and roma_2[idx : idx + 2] in romas.keys():
        arabia_2 += romas[roma_2[idx : idx + 2]]
        idx += 2
    else:
        arabia_2 += romas[roma_2[idx]]
        idx += 1

# 아라비아 숫자를 출력
arabia = arabia_1 + arabia_2
print(arabia)

# 로마 숫자를 출력
while arabia >= 1000:
    print('M', end='')
    arabia -= 1000
while arabia >= 900:
    print('CM', end='')
    arabia -= 900
while arabia >= 500:
    print('D', end='')
    arabia -= 500
while arabia >= 400:
    print('CD', end='')
    arabia -= 400
while arabia >= 100:
    print('C', end='')
    arabia -= 100
while arabia >= 90:
    print('XC', end='')
    arabia -= 90
while arabia >= 50:
    print('L', end='')
    arabia -= 50
while arabia >= 40:
    print('XL', end='')
    arabia -= 40
while arabia >= 10:
    print('X', end='')
    arabia -= 10
while arabia >= 9:
    print('IX', end='')
    arabia -= 9
while arabia >= 5:
    print('V', end='')
    arabia -= 5
while arabia >= 4:
    print('IV', end='')
    arabia -= 4
while arabia:
    print('I', end='')
    arabia -= 1
