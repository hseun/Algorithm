import sys
input = sys.stdin.readline

recursion_count = 0

def recursion(s, l, r):
    global recursion_count
    recursion_count= recursion_count + 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    global recursion_count
    recursion_count = 0
    return recursion(s, 0, len(s) - 1)

for _ in range(int(input())):
    print(isPalindrome(input().strip()), recursion_count)