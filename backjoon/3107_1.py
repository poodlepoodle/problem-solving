import sys

def input(): return sys.stdin.readline().rstrip()

string = input()

# 맨 앞에 ::가 붙은 경우
if string[:2] == '::':
    string = string.replace("::", "0:zeros:")
# 맨 뒤에 ::가 붙은 경우
elif string[-2:] == '::':
    string = string.replace("::", ":zeros:0")
# ::만 있는 경우
elif string == '::':
    string = '0:zeros:0'
else:
    string = string.replace('::', ':zeros:')

string = string.split(':')

if 'zeros' in string:
    idx = string.index('zeros')
    string.remove('zeros')
    for _ in range(8 - len(string)):
        string.insert(idx, '0')

for i in range(len(string)):
    string[i] = string[i].zfill(4)

print(":".join(string))
