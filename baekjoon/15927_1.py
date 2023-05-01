# 백준 15927번: 회문은 회문아니야!!

string = input()

# 케이스 1: 주어진 문자열이 팰린드롬 -> 문자열 길이 - 1
# 케이스 2: 주어진 문자열이 모두 같은 문자 -> -1
# 케이스 3: 주어진 문자열이 팰린드롬이 아님 -> 그냥 문자열 길이

def is_palindrome(string):
    len_string = len(string)

    for idx in range(len_string // 2):
        if string[idx] != string[len_string - 1 - idx]:
            return False
        
    return True

def is_all_same(string):
    letter = string[0]

    for another in string[1:]:
        if letter != another:
            return False
        
    return True

if is_palindrome(string):
    if is_all_same(string):
        print(-1)
    else:
        print(len(string) - 1)
else:
    print(len(string))
